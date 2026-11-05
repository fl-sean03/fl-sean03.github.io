"""Figures for how a force field works. Water as an electron cloud and as balls, springs and charges, and the
five energy terms."""
from functools import lru_cache

import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Circle

import render as rt
import structures as st
from draw import (FLAT, WIDE, angle_arc, arrow, ball_and_stick, canvas, dashed, marker, panel, pt, save, shot, spring,
                  text, text_width)
from style import ACCENT, BLUE, BLUE_SOFT, BODY, INK, MUTED, TEAL, TINT

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
    fig, ax = canvas(*WIDE)
    for x0, title, color in ((0, 'A cloud of electrons', INK), (894, 'Simple rules instead', ACCENT)):
        panel(ax, x0, 0, 834, 714, TINT)
        text(ax, x0 + 44, 58, title, size=32, bold=True, color=color)
    half = np.radians(st.WATER_ANGLE / 2)
    nuclei = np.array([(0, 0, 0), (np.sin(half), -np.cos(half), 0), (-np.sin(half), -np.cos(half), 0)]) * st.WATER_OH
    o, h1, h2 = cloud(ax, nuclei, (417, 360), 120, (69, 132, 696, 528))
    for q in (o, h1, h2):
        ax.add_patch(Circle(q, 7, color='white', zorder=4))
    text(ax, o[0], o[1] - 186, 'oxygen nucleus', size=26, bold=True, ha='center')
    text(ax, o[0], o[1] - 152, '8 protons, 8 neutrons', size=24, color=BODY, ha='center')
    ax.plot([o[0], o[0]], [o[1] - 132, o[1] - 14], color=INK, lw=pt(2), zorder=4)
    text(ax, h1[0] + 40, h1[1] + 150, 'hydrogen nucleus', size=26, bold=True, ha='center')
    text(ax, h1[0] + 40, h1[1] + 184, '1 proton, no neutron', size=24, color=BODY, ha='center')
    ax.plot([h1[0] + 12, h1[0] + 30], [h1[1] + 14, h1[1] + 126], color=INK, lw=pt(2), zorder=4)
    text(ax, 44, 668, 'Quantum chemistry computes this cloud, accurately but slowly', size=24, color=BODY)
    scene = rt.Scene()
    ball_and_stick(scene, ['O', 'H', 'H'], nuclei * 1.9, pairs=[], atom=1.9)
    for hq in nuclei[1:]:
        spring(scene, nuclei[0] * 1.9, hq * 1.9, '#8A93A0', turns=5, radius=0.2, wire=0.06, inset=(0.6, 0.38))
    p = shot(ax, scene, FLAT, (894, 100, 834, 520), 120, centre=(0, -0.55, 0))
    op, hp1, hp2 = (p(q * 1.9) for q in nuclei)
    text(ax, op[0], op[1] - 110, 'δ−', size=40, bold=True, color='#D9483B', ha='center')
    for hp, side in ((hp1, 1), (hp2, -1)):
        text(ax, hp[0] + side * 76, hp[1] + 40, 'δ+', size=40, bold=True, color=BLUE, ha='center')
    text(ax, 1311, 430, 'spring', size=24, color=MUTED, ha='center')
    text(ax, 938, 668, 'Balls, springs and charges are fast enough for millions of atoms', size=24, color=BODY)
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


def spin(ax, centre, rx, ry, color, start=-60, end=230, width=4, head=24):
    """A curved arrow running round an ellipse, for a rotation about an axis."""
    t = np.radians(np.linspace(start, end, 90))
    x, y = centre[0] + rx * np.cos(t), centre[1] - ry * np.sin(t)
    ax.plot(x[:-4], y[:-4], color=color, lw=pt(width), zorder=7, solid_capstyle='round')
    arrow(ax, (x[-5], y[-5]), (x[-1], y[-1]), color=color, width=width, head=head, z=7)


def terms():
    """Ethanol and water with one example of each force-field energy term, numbered as in the sum below."""
    fig, ax = canvas(*WIDE)
    m, q, h, w = ethanol_and_water()
    scene = rt.Scene()
    ball_and_stick(scene, m.symbols, q, m.pairs, atom=1.2, bond=0.16)
    ball_and_stick(scene, ['O', 'H', 'H'], w, atom=1.2, bond=0.16)
    view = rt.view((0, 0.42, 0.91), (0, 1, 0))
    p = shot(ax, scene, view, (0, 0, 1728, 590), 150)
    c1, c2, o, ho, wo = p(q[0]), p(q[1]), p(q[2]), p(q[h]), p(w[0])
    small, big = 0.288 * 150 + 4, 0.432 * 150 + 4  # H and O ball radii in slide px, plus a gap
    # 1: the O-H bond, with a two-way arrow along it
    arrow(ax, o + (0, 64), ho + (0, 64), color=ACCENT, width=3.5, head=18, style='<|-|>')
    marker(ax, *((o + ho) / 2 + (0, 112)), 1, r=26)
    # 2: the C-O-H angle
    marker(ax, *(o + 160 * angle_arc(ax, o, c2, ho, 100, color=ACCENT, width=4)), 2, r=26)
    # 3: twisting about the C-C bond
    spin(ax, (c1 + c2) / 2, 30, 96, ACCENT)
    marker(ax, *((c1 + c2) / 2 + (0, -140)), 3, r=26)
    # 4: van der Waals between a CH2 hydrogen and a water hydrogen
    ch2 = [i for i in range(len(q)) if m.symbols[i] == 'H' and np.linalg.norm(q[i] - q[1]) < 1.2]
    upper = min(ch2, key=lambda i: p(q[i])[1])
    hw = min((1, 2), key=lambda k: p(w[k])[1])
    a, b = p(q[upper]), p(w[hw])
    dashed(ax, a, b, color=TEAL, trim=(small, small))
    marker(ax, *((a + b) / 2 + (0, -48)), 4, r=26, color=TEAL)
    # 5: charges, the hydrogen bond from ethanol O-H to the water O
    dashed(ax, ho, wo, color=BLUE, trim=(small, big))
    marker(ax, *((ho + wo) / 2 + (0, 56)), 5, r=26, color=BLUE)
    parts = ((1, 'bond stretch', ACCENT), (2, 'angle bend', ACCENT), (3, 'twist', ACCENT),
             (4, 'van der Waals', TEAL), (5, 'charges', BLUE))
    text(ax, 0, 664, 'Energy  =', size=34, bold=True)
    x = 190
    for k, (n, word, color) in enumerate(parts):
        marker(ax, x + 26, 664, n, r=26, color=color)
        label = text(ax, x + 64, 664, word, size=30)
        x += 64 + text_width(fig, label) + 48
        if k < len(parts) - 1:
            text(ax, x - 8, 664, '+', size=34, color=MUTED, ha='center')
            x += 26
    return save(fig, 'terms')


FIGURES = (electrons, terms)
