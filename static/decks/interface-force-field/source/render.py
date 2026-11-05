"""Orthographic ray caster for original molecular pictures.

Spheres, cylinders and triangles are traced exactly per pixel into a depth buffer, then shaded
with two lights, depth-based contact shading, outlines and slight depth fog. The returned
projector maps world coordinates (Å) to output pixels so annotations line up with atoms.
"""
import numpy as np
from PIL import Image
from scipy import ndimage


def unit(v):
    v = np.asarray(v, float)
    return v / np.linalg.norm(v)


def view(toward, up=(0, 0, 1)):
    """Rotation whose rows are the camera axes; the viewer sits along `toward`."""
    f = unit(toward)
    r = unit(np.cross(up, f))
    return np.array([r, np.cross(f, r), f])


def rgb(color):
    color = color.lstrip('#')
    return np.array([int(color[i:i + 2], 16) for i in (0, 2, 4)], float) / 255


class Scene:
    def __init__(self):
        self.spheres, self.cylinders, self.triangles = [], [], []

    def sphere(self, center, radius, color):
        self.spheres.append((np.asarray(center, float), float(radius), rgb(color)))

    def cylinder(self, a, b, radius, color_a, color_b=None):
        """A bond: the half nearer `a` in `color_a`, the other half in `color_b` (the same colour if None)."""
        self.cylinders.append((np.asarray(a, float), np.asarray(b, float), float(radius), rgb(color_a),
                               rgb(color_b or color_a)))

    def triangle(self, a, b, c, color, inside=None):
        a, b, c = (np.asarray(p, float) for p in (a, b, c))
        n = np.cross(b - a, c - a)
        if inside is not None and np.dot(n, a - inside) < 0:
            n = -n
        self.triangles.append((a, b, c, unit(n), rgb(color)))

    def polyhedron(self, vertices, color):
        """Convex polyhedron from its corner positions (four for a tetrahedron)."""
        from scipy.spatial import ConvexHull
        vertices = np.asarray(vertices, float)
        centre = vertices.mean(0)
        for face in ConvexHull(vertices).simplices:
            self.triangle(*vertices[face], color, inside=centre)

    def points(self):
        pts = [s[0] for s in self.spheres] + [c[0] for c in self.cylinders] + [c[1] for c in self.cylinders]
        pts += [p for t in self.triangles for p in t[:3]]
        return np.array(pts)


class Projector:
    def __init__(self, rotation, centre, scale, width, height):
        self.rotation, self.centre, self.scale = rotation, centre, scale
        self.width, self.height = width, height

    def camera(self, p):
        return (np.asarray(p, float) - self.centre) @ self.rotation.T

    def __call__(self, p):
        c = self.camera(p)
        return np.stack([self.width / 2 + c[..., 0] * self.scale, self.height / 2 - c[..., 1] * self.scale], -1)


def render(scene, rotation, width, height, scale, centre=None, background='#FFFFFF', supersample=3, outline=1.6,
           contact=1.0, fog=0.22, light=(-0.45, 0.6, 0.8), specular=0.22):
    """Return (RGBA PIL image with an empty background, projector); `scale` is output pixels per Å.

    Fog fades distant atoms toward `background`, which also tints outlines drawn over the empty background.
    `centre` None puts the middle of the scene's bounding box, as the camera sees it, at the image centre.
    """
    rotation = np.asarray(rotation, float)
    if centre is None:
        seen = scene.points() @ rotation.T
        centre = ((seen.min(0) + seen.max(0)) / 2) @ rotation
    centre = np.asarray(centre, float)
    proj = Projector(rotation, centre, scale, width, height)
    ss = supersample
    W, H, s = width * ss, height * ss, scale * ss
    depth = np.full((H, W), -np.inf, np.float32)
    normal = np.zeros((H, W, 3), np.float32)
    color = np.zeros((H, W, 3), np.float32)
    ident = np.full((H, W), -1, np.int32)
    xs = (np.arange(W) + 0.5 - W / 2) / s
    ys = (H / 2 - np.arange(H) - 0.5) / s

    def window(cx, cy, r):
        j0, j1 = int(max(0, (cx - r) * s + W / 2)), int(min(W, (cx + r) * s + W / 2 + 2))
        i0, i1 = int(max(0, H / 2 - (cy + r) * s)), int(min(H, H / 2 - (cy - r) * s + 2))
        return (slice(i0, i1), slice(j0, j1)) if j1 > j0 and i1 > i0 else None

    def write(win, z, n, col, mask, k):
        mask &= z > depth[win]
        if mask.any():
            depth[win][mask] = z[mask]
            normal[win][mask] = n[mask]
            color[win][mask] = col[mask] if col.ndim == 3 else col
            ident[win][mask] = k

    k = 0
    for c, r, col in scene.spheres:
        cc = (c - centre) @ rotation.T
        win = window(cc[0], cc[1], r)
        k += 1
        if win is None:
            continue
        dx, dy = np.broadcast_arrays(xs[win[1]][None, :] - cc[0], ys[win[0]][:, None] - cc[1])
        h2 = r * r - dx * dx - dy * dy
        mask = h2 > 0
        h = np.sqrt(np.maximum(h2, 0))
        z = cc[2] + h
        n = np.stack([dx, dy, h], -1) / r
        write(win, z.astype(np.float32), n, col, mask, k)
    for a, b, r, ca, cb in scene.cylinders:
        a2, b2 = (a - centre) @ rotation.T, (b - centre) @ rotation.T
        axis = b2 - a2
        length = np.linalg.norm(axis)
        u = axis / length
        k += 1
        A = 1 - u[2] ** 2
        if A < 1e-4:
            continue
        lo, hi = np.minimum(a2, b2) - r, np.maximum(a2, b2) + r
        win = window((lo[0] + hi[0]) / 2, (lo[1] + hi[1]) / 2, max(hi[0] - lo[0], hi[1] - lo[1]) / 2)
        if win is None:
            continue
        qx, qy = np.broadcast_arrays(xs[win[1]][None, :] - a2[0], ys[win[0]][:, None] - a2[1])
        qu = qx * u[0] + qy * u[1]
        B = -u[2] * qu
        C = qx * qx + qy * qy - qu * qu - r * r
        disc = B * B - A * C
        mask = disc > 0
        qz = (-B + np.sqrt(np.maximum(disc, 0))) / A
        along = qu + qz * u[2]
        mask &= (along >= 0) & (along <= length)
        perp = np.stack([qx - along * u[0], qy - along * u[1], qz - along * u[2]], -1) / r
        col = np.where((along < length / 2)[..., None], ca, cb)
        write(win, (a2[2] + qz).astype(np.float32), perp, col, mask, k)
    for a, b, c, n, col in scene.triangles:
        v = np.array([(p - centre) @ rotation.T for p in (a, b, c)])
        nn = rotation @ n
        k += 1
        lo, hi = v.min(0), v.max(0)
        win = window((lo[0] + hi[0]) / 2, (lo[1] + hi[1]) / 2, max(hi[0] - lo[0], hi[1] - lo[1]) / 2 + 1 / s)
        det = (v[1, 0] - v[0, 0]) * (v[2, 1] - v[0, 1]) - (v[2, 0] - v[0, 0]) * (v[1, 1] - v[0, 1])
        if win is None or abs(det) < 1e-9:
            continue
        px, py = np.broadcast_arrays(xs[win[1]][None, :] - v[0, 0], ys[win[0]][:, None] - v[0, 1])
        l1 = (px * (v[2, 1] - v[0, 1]) - py * (v[2, 0] - v[0, 0])) / det
        l2 = ((v[1, 0] - v[0, 0]) * py - (v[1, 1] - v[0, 1]) * px) / det
        mask = (l1 >= 0) & (l2 >= 0) & (l1 + l2 <= 1)
        z = v[0, 2] + l1 * (v[1, 2] - v[0, 2]) + l2 * (v[2, 2] - v[0, 2])
        n_img = np.broadcast_to(nn if nn[2] >= 0 else -nn, z.shape + (3,))
        write(win, z.astype(np.float32), n_img, col, mask, k)

    filled = np.isfinite(depth)
    if not filled.any():
        raise ValueError('Nothing to render')
    L1, L2 = unit(light), unit((0.7, -0.15, 0.55))
    diffuse = 0.62 * np.clip(normal @ L1, 0, 1) + 0.16 * np.clip(normal @ L2, 0, 1)
    half = unit(L1 + np.array([0, 0, 1]))
    highlight = specular * np.clip(normal @ half, 0, 1) ** 36
    rim = 0.10 * (1 - np.clip(normal[..., 2], 0, 1)) ** 2
    # Contact shading: pixels lying behind their neighbourhood get darker (depth unsharp masking).
    zmin, zmax = depth[filled].min(), depth[filled].max()
    d = np.where(filled, depth, zmin - 2.0).astype(np.float32)
    occlusion = np.zeros((H, W), np.float32)
    for sigma, weight in ((0.35, 0.55), (1.1, 0.45)):
        f = max(1, int(sigma * s / 4))  # blur a reduced copy; the result is smooth anyway
        small = ndimage.gaussian_filter(d[::f, ::f], sigma * s / f)
        blurred = ndimage.zoom(small, (H / small.shape[0], W / small.shape[1]), order=1)[:H, :W]
        occlusion += weight * np.clip((blurred - d) / 1.2, 0, 1)
    occlusion = np.clip(contact * occlusion, 0, 0.85)
    light_amount = (0.40 * (1 - occlusion) + diffuse * (1 - 0.55 * occlusion))[..., None]
    out = color * light_amount + (highlight + rim)[..., None] * (1 - 0.6 * occlusion[..., None])
    bg = rgb(background)
    if fog and zmax > zmin:
        f = (fog * (zmax - np.where(filled, depth, zmax)) / (zmax - zmin))[..., None]
        out = out * (1 - f) + f * bg
    out = np.where(filled[..., None], np.clip(out, 0, 1), bg)
    alpha = filled.astype(np.float32)
    if outline:
        edge = np.zeros((H, W), bool)
        step = 0.45
        for axis in (0, 1):
            dz = np.abs(np.diff(np.where(filled, depth, zmin - 50), axis=axis))
            other = np.diff(ident, axis=axis) != 0
            crease = np.sum(np.diff(normal, axis=axis) ** 2, -1) > 0.35
            e = (dz > step) | (other & (dz > 0.08)) | (crease & (dz < step))
            if axis == 0:
                edge[1:] |= e
                edge[:-1] |= e
            else:
                edge[:, 1:] |= e
                edge[:, :-1] |= e
        edge = ndimage.binary_dilation(edge, iterations=max(1, int(round(outline * ss / 2 - 0.5))))
        # Edge pixels on the background take the darkened colour of the nearest object.
        idx = ndimage.distance_transform_edt(~filled, return_distances=False, return_indices=True)
        line = 0.38 * color[idx[0], idx[1]]
        out = np.where(edge[..., None], 0.15 * out + 0.85 * line, out)
        alpha = np.maximum(alpha, edge)

    def shrink(a):
        return a.reshape(height, ss, width, ss, *a.shape[2:]).mean((1, 3))

    a = shrink(alpha)
    # Average colour over covered subpixels only, so edges carry no background tint.
    c = shrink(out * alpha[..., None]) / np.maximum(a, 1e-6)[..., None]
    return Image.fromarray((np.clip(np.dstack([c, a]), 0, 1) * 255 + 0.5).astype(np.uint8)), proj
