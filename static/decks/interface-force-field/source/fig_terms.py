"""Figures for how a force field works. Water as an electron cloud and as balls, springs and charges, and the
five energy terms."""
from functools import lru_cache

import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Circle, FancyArrowPatch
from matplotlib.path import Path

import render as rt
import structures as st
from draw import (FLAT, ball_and_stick, canvas, dashed, marker, mix, panel, pt, save, shot, spring, text,
                  text_width)
from style import ACCENT, BLUE, BLUE_SOFT, BODY, ELEMENTS, INK, LINE, MUTED, TEAL, TINT

CLOUD = LinearSegmentedColormap.from_list('cloud', [TINT, BLUE_SOFT, '#9DBCE0', BLUE, '#1F4F86'])  # thin to dense


@lru_cache
def electron_density(nuclei, x, y, step=0.01):
    """Electron density (electrons per Å³) of water, O, H, H at `nuclei` (Å), in its z = 0 plane over the box
    x × y: density functional theory with the PBE functional and the 6-31G(d) basis (PySCF)."""
    from pyscf import dft, gto
    mol = gto.M(atom=list(zip('OHH', nuclei)), basis='6-31g*', unit='Angstrom', verbose=0)
    mf = dft.RKS(mol)
    mf.xc = 'pbe'
    mf.run()
    assert mf.converged
    xs, ys = np.arange(x[0], x[1] + step / 2, step), np.arange(y[0], y[1] + step / 2, step)
    X, Y = np.meshgrid(xs, ys)
    bohr = 0.529177210544
    grid = np.column_stack([X.ravel(), Y.ravel(), np.zeros(X.size)]) / bohr
    rho = dft.numint.eval_rho(mol, dft.numint.eval_ao(mol, grid), mf.make_rdm1()).reshape(X.shape)
    return xs, ys, rho / bohr ** 3


def cloud(ax, nuclei, origin, scale, box):
    """Water's electron density drawn as the deck's blue cloud over the slide-px box (x, y, w, h), with
    `origin` the slide px of (0, 0) Å and contours at 0.01, 0.1 and 1 electron per Å³; returns the nuclei in px."""
    (cx, cy), (x, y, w, h) = origin, box
    xs, ys, rho = electron_density(tuple(map(tuple, nuclei)),
                                   (round((x - cx) / scale, 2), round((x + w - cx) / scale, 2)),
                                   (round((cy - y - h) / scale, 2), round((cy - y) / scale, 2)))
    ax.imshow(np.log10(np.clip(rho, 1e-3, None)), extent=(x, x + w, y + h, y), cmap=CLOUD, vmin=-3, vmax=1.2,
              origin='lower', interpolation='bicubic', zorder=1)
    ax.contour(xs * scale + cx, cy - ys * scale, np.log10(np.clip(rho, 1e-4, None)), levels=[-2, -1, 0],
               colors='white', linewidths=pt(1.2), linestyles='solid', alpha=0.7, zorder=2)
    return [np.array([cx + q[0] * scale, cy - q[1] * scale]) for q in nuclei]


def electrons():
    """Water as quantum chemistry sees it (an electron cloud) and as a force field sees it (balls, springs, charges)."""
    fig, ax = canvas()
    for x0, title, color in ((0, 'A cloud of electrons', INK), (894, 'Simple rules instead', ACCENT)):
        panel(ax, x0, 0, 834, 654, TINT)
        text(ax, x0 + 44, 52, title, size=32, bold=True, color=color)
    half = np.radians(st.WATER_ANGLE / 2)
    nuclei = np.array([(0, 0, 0), (np.sin(half), -np.cos(half), 0), (-np.sin(half), -np.cos(half), 0)]) * st.WATER_OH
    o, h1, h2 = cloud(ax, nuclei, (417, 322), 112, (69, 112, 696, 478))
    for q in (o, h1, h2):
        ax.add_patch(Circle(q, 7, color='white', zorder=4))
    text(ax, o[0], o[1] - 170, 'oxygen nucleus', size=26, bold=True, ha='center')
    text(ax, o[0], o[1] - 138, '8 protons, 8 neutrons', size=24, color=BODY, ha='center')
    ax.plot([o[0], o[0]], [o[1] - 118, o[1] - 14], color=INK, lw=pt(2), zorder=4)
    text(ax, h1[0] + 40, h1[1] + 132, 'hydrogen nucleus', size=26, bold=True, ha='center')
    text(ax, h1[0] + 40, h1[1] + 166, '1 proton, no neutron', size=24, color=BODY, ha='center')
    ax.plot([h1[0] + 12, h1[0] + 28], [h1[1] + 14, h1[1] + 108], color=INK, lw=pt(2), zorder=4)
    text(ax, 44, 616, 'Quantum chemistry computes this cloud, usually at a high cost', size=24, color=BODY)
    scene = rt.Scene()
    ball_and_stick(scene, ['O', 'H', 'H'], nuclei * 1.9, pairs=[], atom=1.9)
    for hq in nuclei[1:]:
        spring(scene, nuclei[0] * 1.9, hq * 1.9, '#8A93A0', turns=5, radius=0.2, wire=0.06, inset=(0.6, 0.38))
    p = shot(ax, scene, FLAT, (894, 92, 834, 488), 112, centre=(0, -0.55, 0))
    op, hp1, hp2 = (p(q * 1.9) for q in nuclei)
    text(ax, op[0], op[1] - 104, 'δ−', size=40, bold=True, color=ELEMENTS['O'][0], ha='center')
    for hp, side in ((hp1, 1), (hp2, -1)):
        text(ax, hp[0] + side * 72, hp[1] + 38, 'δ+', size=40, bold=True, color=BLUE, ha='center')
    text(ax, 1311, 404, 'spring', size=24, color=MUTED, ha='center')
    text(ax, 938, 616, 'Balls, springs and charges often reach millions of atoms', size=24, color=BODY)
    return save(fig, 'electrons')


@lru_cache
def ethanol_and_water():
    """Ethanol (RDKit, MMFF) in its zigzag C-C-O-H form, donating a hydrogen bond to a water.

    The zigzag lies in the x-y plane with O at the origin and O-H along +x. The water O sits 2.85 Å
    from the ethanol O on that line, its plane turned so the bond meets one of its lone pairs."""
    m = st.Molecule('CCO', seed=5)
    h = m.hydrogens(2)[0]
    m.twist(0, 1, 2, h, 180.0)
    p = m.positions
    x = rt.unit(p[h] - p[2])
    y = rt.unit(np.cross(np.cross(x, p[1] - p[2]), x))
    q = (p - p[2]) @ np.array([x, y, np.cross(x, y)]).T
    tilt, half = np.radians(54.74), np.radians(st.WATER_ANGLE / 2)
    o = np.array([2.85, 0, 0])
    bisector = np.array([np.cos(tilt), 0, np.sin(tilt)])
    w = np.array([o] + [o + st.WATER_OH * (np.cos(half) * bisector + side * np.sin(half) * np.array([0, 1, 0]))
                        for side in (1, -1)])
    return m, q, h, w


def along(ax, points, color, width=3.5, head=16, style='<|-|>'):
    """An arrow following a curve of slide-px points."""
    ax.add_patch(FancyArrowPatch(path=Path(np.asarray(points, float)), arrowstyle=style, mutation_scale=pt(head),
                                 color=color, lw=pt(width), zorder=8, capstyle='round', joinstyle='round'))


def circle(centre, u, v, radius, angles):
    """Points at `angles` (radians) on the circle round `centre` spanned by the unit vectors u and v."""
    angles = np.asarray(angles, float)[:, None]
    return centre + radius * (np.cos(angles) * u + np.sin(angles) * v)


TERMS = ((1, 'Bond stretch', ('A bond stretches and', 'squeezes like a spring'), ACCENT),
         (2, 'Angle bend', ('The angle between two', 'bonds bends like a spring'), ACCENT),
         (3, 'Twist', ('A group of atoms turns', 'around a bond'), ACCENT),
         (4, 'Van der Waals', ('Atoms that are not bonded', 'pull weakly on each other'), TEAL),
         (5, 'Charges', ('Opposite partial charges', 'attract each other'), BLUE))


def terms():
    """The five kinds of energy term, one panel each on the same ethanol and water: only the atoms involved keep
    their colour, and each motion is drawn on the real geometry."""
    fig, ax = canvas()
    m, q, h, w = ethanol_and_water()
    symbols, pos = m.symbols + ['O', 'H', 'H'], np.vstack([q, w])
    water = len(q)  # the water oxygen; its first hydrogen is on the carbons' side
    pairs = m.pairs + [(water, water + 1), (water, water + 2)]
    methyl, near = m.hydrogens(0), max(m.hydrogens(1), key=lambda i: q[i][2])  # near: the CH2 hydrogen facing us
    lit = ({2, h}, {1, 2, h}, {0, 1, *methyl}, {near, water + 1}, {h, water})
    view = rt.view((-0.5, 0, 0.75 ** 0.5), (-1, 0, 0))  # upright, ethanol over the water, seen 30° from above
    radii = np.array([ELEMENTS[s][1] * 1.1 for s in symbols])
    seen = pos @ view.T
    lo, hi = (seen[:, :2] - radii[:, None]).min(0), (seen[:, :2] + radii[:, None]).max(0)
    width = (1728 - 3 * 16 - 48) / 5
    scale = min((width - 32) / (hi[0] - lo[0]), 376 / (hi[1] - lo[1]))  # the same size in every panel
    centre = view.T @ [*(lo + hi) / 2, 0]
    # The twist turns the methyl hydrogens round the C-C bond: an arrow round that axis in front of them
    axis = rt.unit(pos[1] - pos[0])
    hub = pos[0] + ((pos[methyl] - pos[0]) @ axis).mean() * axis
    u = rt.unit(np.cross(axis, view[2]))
    v = np.cross(axis, u)
    front = np.arctan2(v @ view[2], u @ view[2])
    turn = circle(hub, u, v, 1.5, front + np.radians(np.linspace(-105, 105, 80)))
    xs = [k * (width + 16) + 32 * (k > 2) for k in range(5)]
    ring = radii * scale + 7  # px, a ring just outside a ball
    for x, (n, title, caption, color), atoms in zip(xs, TERMS, lit):
        panel(ax, x, 34, width, 548)
        marker(ax, x + 40, 76, n, r=22, color=color)
        text(ax, x + 74, 76, title, size=26, bold=True)
        for j, line in enumerate(caption):
            text(ax, x + 24, 118 + 29 * j, line, size=22, color=BODY)
        scene = rt.Scene()
        colors = [ELEMENTS[s][0] if i in atoms else mix(ELEMENTS[s][0], amount=0.7) for i, s in enumerate(symbols)]
        ball_and_stick(scene, symbols, pos, pairs, atom=1.1, colors=colors)
        p = shot(ax, scene, view, (x + 8, 170, width - 16, 404), scale, centre=centre, background=TINT)
        if n == 1:  # a two-way arrow beside the O-H bond and parallel to it, on the side away from the carbons
            a, b = p(pos[2]), p(pos[h])
            d = rt.unit(b - a)
            side = np.array([-d[1], d[0]])
            side *= -np.sign(side @ (p(pos[1]) - a))
            along(ax, [a + 38 * side - 10 * d, b + 38 * side + 10 * d], color)
        elif n == 2:  # an arc round the oxygen in the C-O-H plane, between the two bonds
            c, oh = pos[1] - pos[2], pos[h] - pos[2]
            spread = np.degrees(np.arccos(rt.unit(c) @ rt.unit(oh)))
            arc = circle(pos[2], rt.unit(c), rt.unit(np.cross(np.cross(c, oh), c)), 0.68,
                         np.radians(np.linspace(15, spread - 15, 40)))
            along(ax, p(arc), color)
        elif n == 3:
            along(ax, p(turn), color, width=4, head=22, style='-|>')
        else:  # a dotted line between the two ringed atoms, with their partial charges for the Coulomb pair
            i, j = (near, water + 1) if n == 4 else (h, water)
            a, b = p(pos[i]), p(pos[j])
            dashed(ax, a, b, color=color, trim=(ring[i] + 2, ring[j] + 2))
            for k in (i, j):
                ax.add_patch(Circle(p(pos[k]), ring[k], fc='none', ec=color, lw=pt(3), zorder=7))
            if n == 5:
                text(ax, a[0] - ring[i] - 10, a[1], 'δ+', size=30, bold=True, color=BLUE, ha='right')
                text(ax, b[0] - ring[j] - 10, b[1], 'δ−', size=30, bold=True, color=ELEMENTS['O'][0], ha='right')
    for first, last, label in ((0, 2, 'ALONG THE BONDS'), (3, 4, 'BETWEEN ATOMS THAT ARE NOT BONDED')):
        mark = text(ax, xs[first] + 4, 14, label, size=18, bold=True, color=MUTED)
        ax.plot([xs[first] + 18 + text_width(fig, mark), xs[last] + width], [14, 14], color=LINE, lw=pt(2), zorder=1)
    x = text_width(fig, text(ax, 0, 622, 'Energy  =', size=32, bold=True)) + 22
    for n, *_, color in TERMS:
        marker(ax, x + 22, 622, n, r=22, color=color)
        if n < 5:
            text(ax, x + 66, 622, '+', size=32, color=MUTED, ha='center')
        x += 88
    text(ax, x - 16, 622, 'added up over every bond, angle, twist and pair of atoms', size=24, color=BODY)
    return save(fig, 'terms')


FIGURES = (electrons, terms)
