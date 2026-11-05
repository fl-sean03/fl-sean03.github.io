"""What every figure shares. A canvas laid out in slide pixels, the deck's marks (markers, arrows, panels and
charts), ray-traced pictures placed on the canvas without resampling, and the scenes several figures reuse."""
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.patches import Arc, Circle, FancyArrowPatch, FancyBboxPatch
from PIL import Image
from scipy.spatial import cKDTree

import render as rt
import structures as st
from style import ACCENT, ASSETS, BODY, ELEMENTS, INK, LINE, MUTED, SOURCE, TINT

K = 1.25  # output pixels per slide pixel: figures are laid out on the 1920 × 1080 slide grid
WIDE = (1728, 714)  # the figure box between a one-line title and the takeaway line
LEDE = (1728, 654)  # the same box when a one-line lede sits under the title
FLAT = rt.view((0, 0, 1), (0, 1, 0))  # the x-y plane face on, +y up the screen
CRYSTAL_VIEWS = {'cube': rt.view((0.62, -0.78, 0.52)), 'tetra': rt.view((0.15, 1.0, 0.25), (-1, 1, 1))}


def pt(px):
    """Slide pixels to matplotlib points."""
    return px * K * 72 / 100


for weight in ('Regular', 'Bold'):
    font_manager.fontManager.addfont(str(SOURCE / 'fonts' / f'Lato-{weight}.ttf'))
plt.rcParams.update({
    'font.family': 'Lato', 'font.size': pt(24), 'text.color': INK, 'axes.labelcolor': BODY,
    'axes.edgecolor': LINE, 'axes.linewidth': pt(1.6), 'xtick.color': MUTED, 'ytick.color': MUTED,
    'xtick.labelsize': pt(22), 'ytick.labelsize': pt(22), 'axes.labelsize': pt(24),
    'axes.spines.top': False, 'axes.spines.right': False, 'axes.facecolor': 'none',
    'figure.facecolor': 'white', 'xtick.major.size': 0, 'ytick.major.size': 0,
    'xtick.major.pad': pt(10), 'ytick.major.pad': pt(10), 'lines.solid_capstyle': 'round',
    'savefig.facecolor': 'white', 'mathtext.default': 'regular',
})


def canvas(width, height):
    """A figure laid out in slide pixels with the origin at the top left."""
    fig = plt.figure(figsize=(width * K / 100, height * K / 100), dpi=100)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_xlim(0, width)
    ax.set_ylim(height, 0)
    ax.axis('off')
    ax.set_autoscale_on(False)  # images and patches must not move the slide-pixel frame
    return fig, ax


def save(fig, name, quality=None):
    """PNG for flat graphics; JPEG (quality given) for shaded renders."""
    ASSETS.mkdir(exist_ok=True)
    if quality:
        path = ASSETS / f'{name}.jpg'
        fig.savefig(path, dpi=100, pil_kwargs={'quality': quality, 'optimize': True, 'progressive': True,
                                                'subsampling': 0})
    else:
        path = ASSETS / f'{name}.png'
        fig.savefig(path, dpi=100, metadata={'Software': None})
    plt.close(fig)
    return path


# Marks -----------------------------------------------------------------------------------------------

def mix(color, other='#FFFFFF', amount=0.5):
    """Blend two hex colours; amount 0 keeps `color`."""
    c = rt.rgb(color) * (1 - amount) + rt.rgb(other) * amount
    return '#' + ''.join(f'{round(255 * v):02X}' for v in c)


def text(ax, x, y, s, size=26, color=INK, bold=False, ha='left', va='center', z=6, **kw):
    return ax.text(x, y, s, fontsize=pt(size), color=color, fontweight='bold' if bold else 'normal',
                   ha=ha, va=va, zorder=z, **kw)


def text_width(fig, label):
    """A text label's width in slide px."""
    return label.get_window_extent(fig.canvas.get_renderer()).width / K


def marker(ax, x, y, n, r=22, color=ACCENT):
    ax.add_patch(Circle((x, y), r, color=color, zorder=8))
    text(ax, x, y + 1, str(n), size=r * 1.25, color='white', bold=True, ha='center', va='center_baseline', z=9)


def dashed(ax, a, b, color=ACCENT, width=3.5, z=7, trim=(0, 0)):
    """A dotted pair line from a to b, shortened by `trim` slide px at each end (to stop at the balls)."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    u = (b - a) / np.linalg.norm(b - a)
    ax.plot(*np.transpose([a + trim[0] * u, b - trim[1] * u]), color=color, lw=pt(width), ls=(0, (1.6, 1.8)),
            dash_capstyle='round', zorder=z)


def angle_arc(ax, vertex, a, b, radius, color=INK, width=2.5):
    """Mark the angle at `vertex` between the rays to a and b (slide px); returns the bisector direction."""
    vertex = np.asarray(vertex, float)
    lo, hi = sorted(np.degrees(np.arctan2(*(np.asarray(p, float) - vertex)[::-1])) for p in (a, b))
    if hi - lo > 180:
        lo, hi = hi, lo + 360
    ax.add_patch(Arc(vertex, 2 * radius, 2 * radius, theta1=lo, theta2=hi, color=color, lw=pt(width), zorder=7))
    middle = np.radians((lo + hi) / 2)
    return np.array([np.cos(middle), np.sin(middle)])


def arrow(ax, a, b, color=MUTED, width=4, head=26, rad=0.0, z=5, style='-|>'):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, mutation_scale=pt(head), color=color, lw=pt(width),
                                 connectionstyle=f'arc3,rad={rad}', zorder=z, shrinkA=0, shrinkB=0))


def dimension(ax, a, b, shift, color=INK):
    """A dimension line from centre a to centre b drawn `shift` slide px away, with lines back to dots on the
    centres."""
    a, b, shift = (np.asarray(v, float) for v in (a, b, shift))
    for end in (a, b):
        ax.plot(*np.transpose([end, end + 1.12 * shift]), color=INK, lw=pt(1.6), zorder=7)
        ax.add_patch(Circle(end, 5.5, color=INK, zorder=8))
    arrow(ax, a + shift, b + shift, color=color, width=2.5, head=14, style='<|-|>', z=8)


def panel(ax, x, y, w, h, color=TINT, edge=None, z=0, radius=18):
    return ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad=0,rounding_size={radius}', fc=color,
                                ec=edge or 'none', lw=pt(2), zorder=z))


def result(fig, ax, lead, rest, color):
    """The band under an example: one sentence whose bold, coloured opening says where the number comes from."""
    panel(ax, 0, 578, 1728, 76)
    lead = text(ax, 40, 616, lead, size=26, bold=True, color=color)
    text(ax, 40 + text_width(fig, lead), 616, rest, size=26)


# Charts ----------------------------------------------------------------------------------------------

def chart(fig, ax, box, xlim, ylim, xlabel=None, ylabel=None):
    """A data axes over the slide-pixel box (x, y, w, h) of a canvas made by `canvas`."""
    width, height = ax.get_xlim()[1], ax.get_ylim()[0]
    x, y, w, h = box
    c = fig.add_axes((x / width, 1 - (y + h) / height, w / width, h / height))
    c.set(xlim=xlim, ylim=ylim)
    c.set_xlabel(xlabel or '')
    c.set_ylabel(ylabel or '')
    return c


def curve(c, x, y, color=INK, width=5, z=3, **kw):
    return c.plot(x, y, color=color, lw=pt(width), zorder=z, solid_capstyle='round', **kw)


def dot(c, x, y, color=INK, size=16):
    """A data point on chart `c`, ringed in white."""
    c.scatter([x], [y], s=pt(size) ** 2, color=color, zorder=5, edgecolor='white', linewidth=pt(2.5), clip_on=False)


def at(c, x, y):
    """Slide px of the data point (x, y) on chart `c`."""
    fx, fy = c.transData.transform((x, y))
    return np.array([fx, c.figure.get_figheight() * c.figure.dpi - fy]) / K


# Pictures --------------------------------------------------------------------------------------------

def front_view(elevation):
    """A camera in front of a surface (on its −y side), raised `elevation` degrees above it."""
    a = np.radians(elevation)
    return rt.view((0, -np.cos(a), np.sin(a)))


def place(ax, picture, box, z=2):
    """Put a render made at K output px per slide px into its slide-pixel box without resampling."""
    x, y = (round(v * K) / K for v in box[:2])
    w, h = picture.width / K, picture.height / K
    return ax.imshow(np.asarray(picture), extent=(x, x + w, y + h, y), interpolation='none', aspect='auto',
                     zorder=z)


def fade_edges(picture, left=0, top=0, right=0, bottom=0):
    """Fade an RGBA render to transparent over the given widths in output pixels."""
    a = np.asarray(picture).astype(float)
    h, w = a.shape[:2]
    ramp = np.ones((h, w))
    for size, coord, flip, axis in ((left, np.arange(w), False, 1), (right, np.arange(w), True, 1),
                                    (top, np.arange(h), False, 0), (bottom, np.arange(h), True, 0)):
        if size:
            t = np.clip(((coord[::-1] if flip else coord) + 0.5) / size, 0, 1)
            t = t * t * (3 - 2 * t)
            ramp *= t[None, :] if axis else t[:, None]
    a[..., 3] *= ramp
    return Image.fromarray(a.round().astype(np.uint8))


def shot(ax, scene, rotation, box, scale, centre=None, z=2, **options):
    """Render at `scale` slide px per Å into the slide-pixel box (x, y, w, h); returns Å → slide px."""
    x, y, w, h = (round(v * K) for v in box)
    picture, project = rt.render(scene, rotation, w, h, scale=scale * K, centre=centre, **options)
    place(ax, picture, box, z)
    return lambda p: project(p) / K + (x / K, y / K)


def aim(rotation, point, offset=(0, 0), scale=1.0):
    """The render centre that puts world `point` `offset` slide px (right, down) from the middle at `scale`."""
    return np.asarray(point, float) - np.asarray(rotation).T @ (offset[0] / scale, -offset[1] / scale, 0)


def layered(ax, layers, rotation, box, scale, centre, z=2, supersample=2, edges=None, **options):
    """Render each scene separately and stack them, so a pale front layer casts no contact shadow.

    `edges` fades the stack to transparent over the given widths in slide px, e.g. {'left': 60}."""
    x, y, w, h = (round(v * K) for v in box)
    for n, (scene, extra) in enumerate(layers):
        picture, project = rt.render(scene, rotation, w, h, scale=scale * K, centre=centre, supersample=supersample,
                                     **{**options, **extra})
        if edges:
            picture = fade_edges(picture, **{k: round(v * K) for k, v in edges.items()})
        place(ax, picture, box, z + n * 0.1)
    return lambda p: project(p) / K + (x / K, y / K)


# Scenes ----------------------------------------------------------------------------------------------

def ball_and_stick(scene, symbols, positions, pairs=None, atom=1.0, bond=0.13, fade=0.0, colors=None):
    """Atoms at `atom` × their ball radius joined by two-colour bonds; `fade` blends toward white."""
    positions = np.asarray(positions, float)
    pairs = st.bonds(symbols, positions) if pairs is None else pairs
    colors = [mix(c, amount=fade) for c in (colors or [ELEMENTS[s][0] for s in symbols])]
    for s, p, c in zip(symbols, positions, colors):
        scene.sphere(p, ELEMENTS[s][1] * atom, c)
    for i, j in pairs:
        scene.cylinder(positions[i], positions[j], bond, colors[i], colors[j])


def spheres(scene, symbols, positions, fade=0.0):
    """Touching spheres at each element's metallic or ionic radius."""
    for s, p in zip(symbols, positions):
        scene.sphere(p, ELEMENTS[s][1], mix(ELEMENTS[s][0], amount=fade))


def polyhedral(scene, symbols, positions, centres=('Si', 'P'), fade=0.0):
    """A mineral as SiO4/PO4 tetrahedra and Ca ions, with OH as ball-and-stick and lone oxide ions as small balls."""
    symbols, positions = np.asarray(symbols), np.asarray(positions, float)
    color = {s: mix(ELEMENTS[s][0], amount=fade) for s in set(symbols)}
    tree = cKDTree(positions)
    grouped = set()
    for i in np.flatnonzero(np.isin(symbols, centres)):
        o = [j for j in tree.query_ball_point(positions[i], 1.8) if symbols[j] == 'O']
        if len(o) == 4:
            scene.polyhedron(positions[o], color[symbols[i]])
            grouped.update(o)
    hydroxide = {}
    for i in np.flatnonzero(symbols == 'H'):
        hydroxide[tree.query(positions[i], k=2)[1][1]] = i
    for i, s in enumerate(symbols):
        if s == 'Ca':
            scene.sphere(positions[i], ELEMENTS['Ca'][1], color['Ca'])
        elif i in hydroxide:
            h = hydroxide[i]
            scene.sphere(positions[i], 0.42, color['O'])
            scene.sphere(positions[h], 0.3, color['H'])
            scene.cylinder(positions[i], positions[h], 0.13, color['O'], color['H'])
        elif s == 'O' and i not in grouped:
            scene.sphere(positions[i], 0.5, color['O'])


def spring(scene, a, b, color, turns=4, radius=0.13, wire=0.04, inset=(0.3, 0.2)):
    """A coil spring drawn along the bond a-b, leaving `inset` Å bare at each end."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    u = rt.unit(b - a)
    v = rt.unit(np.cross(u, (0, 0, 1) if abs(u[2]) < 0.9 else (1, 0, 0)))
    w = np.cross(u, v)
    length = np.linalg.norm(b - a)
    t = np.linspace(0, 1, turns * 20 + 1)
    phase = 2 * np.pi * turns * t
    coil = (a + np.outer(inset[0] + t * (length - sum(inset)), u)
            + radius * (np.outer(np.cos(phase), v) + np.outer(np.sin(phase), w)))
    for p, q in zip(coil[:-1], coil[1:]):
        scene.cylinder(p, q, wire, color)
        scene.sphere(q, wire, color)


def backing(scene, positions, color, below=0.6):
    """A dark floor under a slab, so the hollows between touching spheres never show the background."""
    lo, hi = positions.min(0) - 2, positions.max(0) + 2
    z = lo[2] + 2 - below
    corners = [(lo[0], lo[1], z), (hi[0], lo[1], z), (hi[0], hi[1], z), (lo[0], hi[1], z)]
    scene.triangle(corners[0], corners[1], corners[2], color, inside=(0, 0, z - 1))
    scene.triangle(corners[0], corners[2], corners[3], color, inside=(0, 0, z - 1))


def platinum_scenes(m, pep, metal, water, ring=False, fade=0.62):
    """Two scenes for `layered`, a peptide (molecule m at positions `pep`) on a metal surface and the water around
    them faded toward white. Metal and water are (symbols, positions); `ring` colours the peptide's phenylalanine
    ring carbons."""
    marked = set(m.ring()) if ring else set()
    colors = [ACCENT if i in marked and e == 'C' else ELEMENTS[e][0] for i, e in enumerate(m.symbols)]
    solid, liquid = rt.Scene(), rt.Scene()
    spheres(solid, *metal)
    backing(solid, metal[1], mix(ELEMENTS['Pt'][0], INK, 0.55))
    ball_and_stick(solid, m.symbols, pep, m.pairs, colors=colors)
    ball_and_stick(liquid, *water, fade=fade)
    return solid, liquid


def pt_crystal(shape, size):
    """An ideal Pt nanocrystal scene: a cube has square-pattern faces, a tetrahedron triangular ones."""
    scene = rt.Scene()
    atoms = st.nanocrystal('Pt', shape, size).positions
    spheres(scene, ['Pt'] * len(atoms), atoms)
    return scene


def magnifier(ax, centre, radius, face, ring_color, scale=15):
    """A round inset showing the atom pattern of one Pt face from above, square for (100) and triangular for (111)."""
    a, n = st.LATTICE['Pt'] / np.sqrt(2), 5
    if face == '100':
        atoms = [(i * a, j * a, 0) for i in range(-n, n + 1) for j in range(-n, n + 1)]
    else:
        atoms = [((i + j / 2) * a, j * a * np.sqrt(3) / 2, 0) for i in range(-n - 3, n + 4) for j in range(-n, n + 1)]
    scene = rt.Scene()
    for p in atoms:
        scene.sphere(p, ELEMENTS['Pt'][1], ELEMENTS['Pt'][0])
    x, y = centre
    box = (x - radius, y - radius, 2 * radius, 2 * radius)
    picture, _ = rt.render(scene, FLAT, round(2 * radius * K), round(2 * radius * K), scale=scale * K,
                           centre=(0, 0, 0), fog=0)
    image = place(ax, picture, box, z=4)
    clip = Circle(centre, radius, transform=ax.transData)
    image.set_clip_path(clip)
    ax.add_patch(Circle(centre, radius, fc='white', ec='none', zorder=3))
    ax.add_patch(Circle(centre, radius, fc='none', ec=ring_color, lw=pt(5), zorder=5))
