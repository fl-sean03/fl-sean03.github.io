"""Figures for the pair energies and what they add up to. The rhodium Lennard-Jones curve with the pair at its wall,
well and tail, Coulomb's law for charged ions drawn against it at the same scale, and a rhodium block split in two
for its surface energy."""
import numpy as np

import render as rt
import science as sc
import structures as st
from draw import FLAT, LEDE, arrow, at, canvas, chart, curve, dimension, dot, marker, mix, pt, save, shot, text
from style import ACCENT, BLUE, BODY, ELEMENTS, INK, LINE, MUTED, RULE


RH = sc.METALS['Rh']
RH_COLOR = ELEMENTS['Rh'][0]
RH_RADIUS = st.LATTICE['Rh'] * np.sqrt(2) / 4  # touching spheres along the face diagonals
NEW_FACE = mix(ACCENT, amount=0.45)


def pair_icon(ax, centre, distance, radii=(RH[0] / 2,) * 2, colors=(RH_COLOR,) * 2):
    """Two atoms `distance` Å apart, rhodium spheres of diameter r₀ unless radii and colours are given; returns
    their centres and radii in px."""
    scale = 30  # slide px per Å
    a, b = np.array([-distance / 2, 0, 0]), np.array([distance / 2, 0, 0])
    scene = rt.Scene()
    scene.sphere(a, radii[0], colors[0])
    scene.sphere(b, radii[1], colors[1])
    w, h = (distance + 2 * max(radii)) * scale + 16, 2 * max(radii) * scale + 16
    p = shot(ax, scene, FLAT, (centre[0] - w / 2, centre[1] - h / 2, w, h), scale, centre=(0, 0, 0))
    return p(a), p(b), [r * scale for r in radii]


def forces(ax, a, b, radii, sign):
    """Arrows beside a pair: sign +1 pushes the atoms apart, −1 pulls them together."""
    for centre, r, side in ((a, radii[0], -1), (b, radii[1], 1)):
        start = centre + (side * (r + 8), 0)
        tip = start + (side * 26, 0)
        arrow(ax, *((start, tip) if sign > 0 else (tip, start)), color=INK, width=4, head=20)


def lj_chart(fig, ax, xlim, ylim, box=(150, 14, 960, 520)):
    c = chart(fig, ax, box, xlim, ylim, 'Distance between the atom centres (Å)', 'Energy (kcal/mol)')
    c.axhline(0, color=LINE, lw=pt(2), zorder=1)
    return c


def pair_row(ax, y, n, distance, sign, head, line):
    """A numbered row of the right-hand column: the rhodium pair, its centre-to-centre distance and two lines."""
    x = 1186
    marker(ax, x, y, n, r=24)
    a, b, radii = pair_icon(ax, (x + 184, y), float(distance))
    dimension(ax, a, b, (0, 62))
    text(ax, (a[0] + b[0]) / 2, y + 94, f'{distance} Å', size=24, ha='center')
    if sign:
        forces(ax, a, b, radii, sign)
    text(ax, x + 348, y - 18, head, size=28, bold=True)
    text(ax, x + 348, y + 20, line, size=24, color=BODY)


def lj():
    """The rhodium 12-6 pair curve (K21) with its wall, well and tail, and the pair at each."""
    fig, ax = canvas(*LEDE)
    r0, eps = RH
    c = lj_chart(fig, ax, (2.25, 5.6), (-10, 14))
    r = np.linspace(2.25, 5.6, 800)
    curve(c, r, sc.energy(r, *RH), color=RH_COLOR)
    guide = dict(color=LINE, lw=pt(2), ls=(0, (2, 2)), zorder=2)
    c.plot([r0, r0], [-10, -eps], **guide)
    c.plot([r0, 3.5], [-eps, -eps], **guide)
    arrow(ax, at(c, 3.5, 0), at(c, 3.5, -eps), color=INK, width=2.5, head=16, style='<|-|>')
    text(ax, *(at(c, 3.5, -5.0) + (18, 0)), 'depth ε = 7.84 kcal/mol', size=24)
    text(ax, *(at(c, r0, -10) + (14, -22)), 'r₀ = 2.757 Å', size=24)
    for n, (d, offset) in enumerate(((2.4, (48, 0)), (r0, (0, -56)), (4.2, (0, -44))), 1):
        u = sc.energy(d, *RH)
        dot(c, d, u)
        marker(ax, *(at(c, d, u) + offset), n, r=24)
    for n, (d, sign, head, line) in enumerate((('2.4', 1, 'Too close', 'they push apart'),
                                               ('2.757', 0, 'Just right', 'lowest energy'),
                                               ('4.2', -1, 'Far apart', 'a weak pull')), 1):
        pair_row(ax, 78 + 214 * (n - 1), n, d, sign, head, line)
    return save(fig, 'lj')


def coulomb():
    """Two unit charges in vacuum (Coulomb's law) beside the rhodium van der Waals curve, at the same scale."""
    fig, ax = canvas(*LEDE)
    c = lj_chart(fig, ax, (2.0, 10.5), (-170, 170), box=(150, 14, 1000, 520))
    r = np.linspace(2.0, 10.5, 600)
    curve(c, r, sc.coulomb(r, 1, -1), color=BLUE)
    curve(c, r, sc.coulomb(r, 1, 1), color=BLUE, ls=(0, (2.5, 1.6)))
    rr = np.linspace(2.4, 10.5, 600)
    curve(c, rr, sc.energy(rr, *RH), color=RH_COLOR, width=4)
    text(ax, *at(c, 4.6, 92), 'like charges push apart', size=26, color=BLUE)
    text(ax, *at(c, 4.6, -96), 'opposite charges pull together', size=26, color=BLUE)
    text(ax, *at(c, 4.6, 20), 'van der Waals (rhodium)', size=24, color=RH_COLOR)
    for d, label, offset, ha in ((3.0, '−110.7 at 3 Å', (24, 10), 'left'), (10.0, '−33.2 at 10 Å', (-12, 40), 'right')):
        u = float(sc.coulomb(d))
        dot(c, d, u, BLUE)
        text(ax, *(at(c, d, u) + offset), label, size=24, bold=True, color=BLUE, ha=ha)
    u = float(sc.energy(10.0, *RH))
    dot(c, 10.0, u, RH_COLOR)
    text(ax, *(at(c, 10.0, u) + (-12, -32)), f'−{abs(u):.3f} at 10 Å', size=24, bold=True, color=RH_COLOR,
         ha='right')
    colors = {'Na': ELEMENTS['Na'][0], 'Cl': ELEMENTS['Cl'][0]}
    cases = ((('Na', 'Cl'), 2.83, -1, 'Opposite charges attract', 'Na⁺ and Cl⁻, as in table salt'),
             (('Na', 'Na'), 4.2, 1, 'Like charges repel', 'two Na⁺ ions'))
    for k, (ions, distance, sign, head, line) in enumerate(cases):
        y = 120 + 290 * k
        a, b, radii = pair_icon(ax, (1470, y), distance, [st.ION_RADII[i] for i in ions], [colors[i] for i in ions])
        for centre, ion in zip((a, b), ions):
            text(ax, *centre, '+' if ion == 'Na' else '−', size=40, bold=True, color='white', ha='center',
                 va='center_baseline', z=9)
        forces(ax, a, b, radii, sign)
        text(ax, 1470, y + 98, head, size=28, bold=True, ha='center')
        text(ax, 1470, y + 136, line, size=24, color=BODY, ha='center')
    return save(fig, 'coulomb')


def cleave():
    """A rhodium (111) block, then the same block pulled apart into two halves (K21 Table 3)."""
    fig, ax = canvas(*LEDE)
    pos = st.fcc_slab('Rh', '111', (6, 6, 6)).get_positions()
    pos -= [*pos[:, :2].mean(0), pos[:, 2].min()]
    layer = np.round(pos[:, 2] / (st.LATTICE['Rh'] / np.sqrt(3))).astype(int)
    view, gap, scale = rt.view((0.34, -1, 0.5), (0, 0, 1)), 7.0, 19
    centre = (0, 0, (pos[:, 2].max() + gap) / 2)
    for k, split in enumerate((False, True)):
        scene = rt.Scene()
        for q, n in zip(pos, layer):
            fresh = split and n in (2, 3)
            scene.sphere(q + (0, 0, gap if split and n >= 3 else 0), RH_RADIUS, NEW_FACE if fresh else RH_COLOR)
        p = shot(ax, scene, view, (20 + 500 * k, 24, 420, 560), scale, centre=centre)
        text(ax, 230 + 500 * k, 622, ('One block', 'Pulled apart')[k], size=28, bold=True, ha='center')
    middle = p((0, 0, pos[:, 2].max() / 2 + gap / 2 + 1.1))
    arrow(ax, (450, middle[1]), (510, middle[1]), color=MUTED, width=4, head=24)
    for j, line in enumerate(('two new faces,', 'each of area A')):
        text(ax, 950, middle[1] - 18 + 38 * j, line, size=26, bold=True, color=ACCENT)
    x0 = 1250
    text(ax, x0, 120, 'Surface energy =', size=30, bold=True)
    text(ax, x0, 170, 'energy to pull apart ÷ 2A', size=28)
    ax.plot([x0, 1728], [236, 236], color=RULE, lw=pt(2), zorder=1)
    text(ax, x0, 290, 'Rhodium', size=24, bold=True, color=MUTED)
    for k, (who, value) in enumerate((('measured', '2.64 ± 0.02 J/m²'), ('IFF', '2.643 J/m²'))):
        text(ax, x0, 350 + 56 * k, who, size=28, color=BODY)
        text(ax, 1728, 350 + 56 * k, value, size=28, bold=True, ha='right')
    text(ax, x0, 470, 'IFF was tuned to match this', size=22, color=MUTED)
    return save(fig, 'cleave')


FIGURES = (lj, coulomb, cleave)
