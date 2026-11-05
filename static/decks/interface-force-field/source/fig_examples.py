"""Figures for the three published examples. A peptide that tells two platinum faces apart, water on silica, and
hydroxyapatite in acid."""
from functools import lru_cache

import numpy as np
from matplotlib.patches import Circle
from scipy.spatial import cKDTree

import render as rt
import structures as st
from draw import (aim, angle_arc, arrow, ball_and_stick, canvas, front_view, layered, magnifier,
                  platinum_scenes, polyhedral, pt, result, save, text)
from style import ACCENT, BLUE, BODY, ELEMENTS, LINE, MUTED, TEAL


def platinum():
    """S7 in water on Pt(111) and Pt(100): its F ring lies flat on the triangular face and stands up on the square
    one (R13, CHARMM-METAL). Illustrative poses, not simulation snapshots."""
    fig, ax = canvas()
    m, flat, upright = st.s7()
    rotation = front_view(30)
    flat = flat @ st.rotation((0, 0, 1), np.pi).T  # puts the backbone behind the ring, so the ring shows
    panels = (('111', flat, TEAL, 'Triangular face', 'Lies flat and sticks', 'its hexagon fits the triangular pattern'),
              ('100', upright, BLUE, 'Square face', 'Stands up, does not stick',
               'computed +3 kcal/mol, so water keeps the surface'))
    for k, (face, pep, color, title, head, line) in enumerate(panels):
        x0 = 894 * k
        water = st.waters_around((-16, -9, 2.4), (16, 9, 7), pep, rotation, seed=5 + k, margin=0.8)
        solid, liquid = platinum_scenes(m, pep, st.metal_surface((13, 10, 3), face=face), water, ring=True, fade=0.6)
        layered(ax, ((solid, {}), (liquid, {'contact': 0.5})), rotation, (x0, 70, 834, 390), 26,
                centre=aim(rotation, (0, 0, 4.0), (0, 60), 26),
                edges={'left': 80, 'right': 80, 'top': 40, 'bottom': 50})
        magnifier(ax, (x0 + 66, 66), 52, face, color, scale=11)
        text(ax, x0 + 140, 66, title, size=30, bold=True, color=color)
        text(ax, x0 + 417, 492, head, size=28, bold=True, ha='center')
        text(ax, x0 + 417, 532, line, size=24, color=BODY, ha='center')
    result(fig, ax, 'In the lab', ', every peptide version with F grew many tetrahedra, crystals with only '
                                  'triangular faces, and versions without F grew few', ACCENT)
    return save(fig, 'platinum', quality=90)


def wetting():
    """A 14 Å slice through water on hydroxylated silica (Q3, contact angle 0°) and on silica whose OH groups heating
    removed (Q4, 42°) (E14). The film and the 42° droplet are drawn to those angles, not simulated."""
    fig, ax = canvas()
    symbols, positions = st.silica((19, 9, 3), (0, 6, 6.5), (62, 30, 14))
    rotation = front_view(6)
    angle, base, depth = np.radians(42), 16.0, 7.0
    for k, wet in enumerate((True, False)):
        x0 = 894 * k
        keep = [i for i, e in enumerate(symbols) if wet or e != 'H']
        solid = rt.Scene()
        polyhedral(solid, [symbols[i] for i in keep], positions[keep])
        floor = positions[[i for i in keep if symbols[i] == 'O'], 2].max() + 1.0  # lowest water oxygen height
        if wet:
            wsym, wpos = st.water_box((-26, -depth, floor), (26, depth, floor + 2.8), avoid=positions[keep],
                                      clearance=2.4, seed=8)
        else:
            height = base * np.tan(angle / 2)
            radius = base / np.sin(angle)
            centre = np.array((0, 0, floor + height - radius))
            wsym, wpos = st.water_box((-base, -depth, floor), (base, depth, floor + height), avoid=positions[keep],
                                      clearance=2.4, seed=8)
            inside = np.repeat(np.linalg.norm(wpos[::3] - centre, axis=1) < radius, 3)
            wsym, wpos = [e for e, i in zip(wsym, inside) if i], wpos[inside]
        liquid = rt.Scene()
        ball_and_stick(liquid, wsym, wpos, atom=1.2)
        p = layered(ax, ((solid, {}), (liquid, {'contact': 0.5})), rotation, (x0, 0, 834, 460), 22,
                    centre=aim(rotation, (0, 0, 0), (0, 30), 22), edges={'left': 70, 'right': 70, 'bottom': 40})
        if wet:
            y = p((0, 0, floor + 6))[1]
            for start, end in ((x0 + 130, x0 + 50), (x0 + 704, x0 + 784)):
                arrow(ax, (start, y), (end, y), color=MUTED, width=4, head=22)
            continue
        arc = np.linspace(-angle, angle, 60)
        outline = np.array([p(centre + radius * np.array((np.sin(t), 0, np.cos(t)))) for t in arc])
        ax.plot(*outline.T, color=BLUE, lw=pt(2.5), ls=(0, (2, 2)), zorder=7)
        a = p((base, 0, floor))
        b = p((base, 0, floor) + 9 * np.array((-np.cos(angle), 0, np.sin(angle))))
        c = p((base + 2, 0, floor))
        ax.plot([a[0], b[0]], [a[1], b[1]], color=ACCENT, lw=pt(4), zorder=8, solid_capstyle='round')
        ax.plot([p((base - 12, 0, floor))[0], c[0]], [a[1], c[1]], color=ACCENT, lw=pt(4), zorder=8,
                solid_capstyle='round')
        bisector = angle_arc(ax, a, b, p((base - 12, 0, floor)), 70, color=ACCENT, width=3)
        text(ax, *(a + 112 * bisector), '42°', size=28, bold=True, color=ACCENT, ha='center', z=9,
             bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none'))
    for k, (head, line) in enumerate((('OH groups on the surface', 'water spreads flat (0°)'),
                                      ('OH groups removed by heating', 'water beads up (42°)'))):
        text(ax, 894 * k + 417, 492, head, size=28, bold=True, ha='center')
        text(ax, 894 * k + 417, 532, line, size=24, color=BODY, ha='center')
    result(fig, ax, 'The simulated angles', ' came within 3° of the measured ones on every surface tested, including '
                                            'two in between', TEAL)
    return save(fig, 'wetting', quality=90)


@lru_cache
def apatite(ph):
    """Hydroxyapatite's basal (001) face with its top layer, Ca5(PO4)3OH per cell, above pH 14 or at pH 10 or 5
    (L16 eqs 3-6). Below pH 14 the surface OH⁻ leaves with half a Ca²⁺; each top phosphate then takes one H (pH 10)
    or two (pH 5) and half a Ca²⁺ leaves per H. Unrelaxed and illustrative. Returns symbols, positions (top O at
    z = 0) and the positions of the Ca²⁺ that left."""
    bulk = st.hydroxyapatite()
    bulk.positions[:, 2] *= -1  # z → -z maps the crystal onto itself but turns every OH⁻ to point its H up
    bulk.wrap()
    c = bulk.cell.lengths()[2]
    row = bulk.cell.lengths()[0] * np.sin(np.radians(60))  # one row of cells deep
    symbols, positions = st.block(bulk, (5, 2, 2), (0, 0, -0.02 * c), (38, row, 1.945 * c))
    symbols = np.array(symbols)
    frac = np.linalg.solve(bulk.cell.array.T, positions.T).T
    site = np.round(frac[:, :2] % 1, 2)
    top = positions[:, 2] > 1.45 * c
    hydroxide = top & ~np.isin(symbols, ('Ca', 'P')) & np.all(np.isclose(site, 0) | np.isclose(site, 1), axis=1)
    calcium2 = top & (symbols == 'Ca') & (positions[:, 2] > 1.7 * c)
    calcium1 = top & (symbols == 'Ca') & ~calcium2
    gone = np.zeros(len(symbols), bool)
    hydrogens = []
    if ph < 14:
        gone |= hydroxide
        kept = site[np.flatnonzero(calcium2)[0]]  # one Ca²⁺ of each three around a hydroxide column stays
        gone |= calcium2 & ~np.all(np.isclose(site, kept, atol=0.02), axis=1)
        tree = cKDTree(positions)
        camera = np.array((0, -1.0, 0))
        for i in np.flatnonzero(top & (symbols == 'P')):
            oxygens = sorted((j for j in tree.query_ball_point(positions[i], 1.8) if symbols[j] == 'O'),
                             key=lambda j: -positions[j, 2])
            sites = [oxygens[0]]
            if ph < 10:  # the second H goes on the side oxygen facing the viewer, so it shows
                sites.append(max(oxygens[1:3], key=lambda j: np.dot(positions[j] - positions[i], camera)))
            for j in sites:
                away = rt.unit(positions[j] - positions[i])
                side = camera if abs(away[2]) > 0.9 else np.array((0, 0, 1.0))
                side = rt.unit(side - np.dot(side, away) * away)
                angle = np.radians(180 - 115)  # P−O−H 115°, O−H 0.94 Å (L16 Table 2)
                hydrogens.append(positions[j] + 0.94 * (np.cos(angle) * away + np.sin(angle) * side))
    if ph < 10:
        gone |= calcium2
        cell = np.floor(frac[:, 0] + 1e-6) + np.floor(frac[:, 1] + 1e-6)
        gone |= calcium1 & np.isclose(site[:, 0], 0.33, atol=0.02) & (cell % 2 == 0)
    left = positions[gone & (symbols == 'Ca')]
    symbols, positions = list(symbols[~gone]) + ['H'] * len(hydrogens), np.vstack([positions[~gone], *hydrogens])
    shift = np.array([*positions[:, :2].mean(0), positions[np.array(symbols) == 'O', 2].max()])
    return symbols, positions - shift, left - shift


def apatites():
    """A one-cell-thick slice of hydroxyapatite as the water around it turns acidic (L16): phosphate gains H⁺ and
    Ca²⁺ leaves. The layers below the top one are faded; dotted rings mark where Ca²⁺ left."""
    fig, ax = canvas()
    rotation = front_view(20)
    scale = 24
    labels = {14: (('phosphate', 'P', -8.0), ('calcium', 'Ca', 3.6), ('hydroxide', 'OH', 10.0)),
              10: (('H⁺ joins', 'H', -5.0), ('Ca²⁺ left', 'left', 3.5)),
              5: (('another H⁺', 'H2', -1.0),)}
    for k, ph in enumerate((14, 10, 5)):
        x0 = 590 * k
        symbols, positions, left = apatite(ph)
        e = np.array(symbols)
        top = positions[:, 2] > -3.2
        scene = rt.Scene()
        polyhedral(scene, list(e[~top]), positions[~top], fade=0.62)
        polyhedral(scene, list(e[top]), positions[top])
        p = layered(ax, ((scene, {}),), rotation, (x0, 40, 548, 430), scale,
                    centre=aim(rotation, (0, 0, 0), (0, -95), scale), edges={'left': 60, 'right': 60, 'bottom': 90})
        for q in left:
            if x0 + 70 < p(q)[0] < x0 + 478:
                ax.add_patch(Circle(p(q), ELEMENTS['Ca'][1] * scale, fc='none', ec=ELEMENTS['Ca'][0], lw=pt(3),
                                    ls=(0, (1.2, 1.2)), zorder=5))
        z = positions[:, 2]
        kinds = {'P': (e == 'P') & top, 'Ca': (e == 'Ca') & (z > -1.6), 'OH': (e == 'O') & (z > -1.0) & (z < -0.6),
                 'H': (e == 'H') & (z > 0.2), 'H2': (e == 'H') & (z > -0.6) & (z < -0.2)}
        for word, kind, x in labels[ph]:
            pool = left[left[:, 2] > -1.6] if kind == 'left' else positions[kinds[kind]]
            target = pool[np.argmin(np.abs(pool[:, 0] - x) + 0.3 * pool[:, 1])]
            tx, ty = p(target + (0, 0, 1.3 if kind == 'P' else 0))
            text(ax, tx, 72, word, size=22, color=BODY, ha='center')
            ax.plot([tx, tx], [88, ty - 16], color=MUTED, lw=pt(1.5), zorder=7)
        text(ax, x0 + 274, 20, 'pH > 14' if ph == 14 else f'pH {ph}', size=32, bold=True, ha='center')
        if k < 2:
            arrow(ax, (x0 + 360, 20), (x0 + 778, 20), color=LINE, width=3, head=20)
    for k, (head, line) in enumerate((('The bare crystal', 'PO₄³⁻ on top, stable only at very high pH'),
                                      ('One H on each phosphate', 'HPO₄²⁻, with hydroxide and some Ca²⁺ gone'),
                                      ('Two H on each phosphate', 'H₂PO₄⁻, with more Ca²⁺ gone'))):
        text(ax, 590 * k + 274, 498, head, size=28, bold=True, ha='center')
        text(ax, 590 * k + 274, 538, line, size=23, color=BODY, ha='center')
    result(fig, ax, 'The simulated mineral', ' gives off 619 mJ/m² as water wets it at pH 7 (533 if all faces count '
                                             'equally), and experiments find 600–700', TEAL)
    return save(fig, 'apatites', quality=90)


FIGURES = (platinum, wetting, apatites)
