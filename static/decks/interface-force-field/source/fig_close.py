"""Figures for the close. The author's described IFF Agent workflow, drawn step by step with rhodium's published
numbers, and the closing bookend."""
import itertools

import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle

import render as rt
import science as sc
import structures as st
from draw import (CRYSTAL_VIEWS, FLAT, arrow, backing, ball_and_stick, canvas, front_view, marker, mix, panel,
                  pt, result, save, shot, spheres, spring, text, text_width)
from fig_opening import s7_on_platinum
from fig_pairs import RH, RH_COLOR
from style import ACCENT, BLUE, BODY, INK, LINE, MUTED, RULE, TEAL, TINT


AGENT = (('Ask', ('rhodium faces', 'in water')),
         ('Gather', ('measured size,', 'surface energy', 'and stiffness')),
         ('Choose', ('a 12-6 pair', 'curve with r₀ and ε')),
         ('Plan', ('tune size and', 'surface energy,', 'test stiffness')),
         ('Fit', ('r₀ = 2.757 Å', 'ε = 7.84 kcal/mol')),
         ('Test', ('stretching is', '209 vs 379 GPa,', '45% low')),
         ('Read back', ('energy at r₀ is', '−7.84, not 0')),
         ('Decide', ('use for surfaces,', 'flag stiffness')))


def page(ax, x, y, w, h, chart=False):
    """A sheet of paper with a folded corner and lines of text, its top left at (x, y); `chart` adds measured
    points."""
    fold = 0.24 * w
    ax.add_patch(Polygon([(x, y), (x + w - fold, y), (x + w, y + fold), (x + w, y + h), (x, y + h)], fc='white',
                         ec=LINE, lw=pt(2.5), joinstyle='round', zorder=4))
    ax.add_patch(Polygon([(x + w - fold, y), (x + w - fold, y + fold), (x + w, y + fold)], fc=RULE, ec=LINE,
                         lw=pt(2.5), joinstyle='round', zorder=4))
    rows = 2 if chart else 4
    for j in range(rows):
        ax.plot([x + 0.15 * w, x + (0.55 if j == 0 else 0.8) * w], [y + 0.12 * h + fold * 0.6 + 15 * j] * 2,
                color=LINE, lw=pt(4), zorder=5)
    if chart:  # a small plot of measured points
        left, bottom, top = x + 0.15 * w, y + 0.88 * h, y + 0.5 * h
        ax.plot([left, left, x + 0.85 * w], [top, bottom, bottom], color=MUTED, lw=pt(2), zorder=5)
        for k, f in enumerate((0.25, 0.45, 0.6, 0.8)):
            ax.add_patch(Circle((left + f * 0.7 * w, bottom - (0.15 + 0.2 * k) * (bottom - top)), 4.5, color=INK,
                                zorder=6))


def badge(ax, x, y, r, color):
    """A filled circle holding a white tick."""
    ax.add_patch(Circle((x, y), r, color=color, zorder=6))
    ax.plot(*np.transpose([(x + r * u, y + r * v) for u, v in ((-0.45, 0.02), (-0.12, 0.36), (0.48, -0.36))]),
            color='white', lw=pt(0.2 * r), zorder=7, solid_joinstyle='round')


def flag(ax, x, y, h, color):
    """A pennant on a pole standing at (x, y)."""
    ax.plot([x, x], [y, y - h], color=INK, lw=pt(3.5), zorder=6)
    ax.add_patch(Polygon([(x, y - h), (x + 0.7 * h, y - 0.8 * h), (x, y - 0.6 * h)], color=color, zorder=6))


def sketch(ax, box, curves, rlim=(2.15, 5.0), elim=(-9.5, 9.0)):
    """Small axes in the slide-px box with 12-6 curves [(r0, epsilon, line style)]; returns (r, E) to slide px."""
    # Drawn on the canvas itself, not as a chart() axes, so the arrows and dot marked on it can sit above its curves
    x, y, w, h = box

    def px(r, e):
        return np.array([x + (np.asarray(r) - rlim[0]) / (rlim[1] - rlim[0]) * w,
                         y + (elim[1] - np.asarray(e)) / (elim[1] - elim[0]) * h])
    ax.plot([x, x, x + w], [y, y + h, y + h], color=MUTED, lw=pt(2), zorder=3)
    ax.plot(*np.transpose([px(rlim[0], 0), px(rlim[1], 0)]), color=RULE, lw=pt(2), zorder=2)
    for r0, eps, style in curves:
        r = np.linspace(r0 * 0.85, rlim[1], 300)
        e = sc.energy(r, r0, eps)
        ax.plot(*px(r[e <= elim[1]], e[e <= elim[1]]), zorder=4, **style)
    return px


def rhodium_face(size):
    """A rhodium (111) slab as touching spheres over a dark floor."""
    scene = rt.Scene()
    slab = st.metal_surface(size, 'Rh')
    spheres(scene, *slab)
    backing(scene, slab[1], mix(RH_COLOR, INK, 0.55))
    return scene


def agent():
    """The author's described IFF Agent workflow, each step drawn with rhodium's published K21 values: the face in
    water, the papers and measurements, the pair curve, the crystal's repeating cube, the fitted curve, the
    stiffness test, the readback of the exported numbers and the decision. An illustration, not a new fit."""
    fig, ax = canvas()
    for k, (title, line, color) in enumerate((('Set up', 'decide what the result must show', BLUE),
                                              ('Run and check', 'compute, test, then decide', TEAL))):
        panel(ax, 876 * k, 0, 852, 548)
        head = text(ax, 876 * k + 32, 48, title, size=30, bold=True, color=color)
        text(ax, 876 * k + 50 + text_width(fig, head), 49, line, size=24, color=MUTED)
    xs = [106.5 + 213 * k + 24 * (k > 3) for k in range(8)]  # column centres; pictures sit between y 150 and 392
    for n, (x, (verb, lines)) in enumerate(zip(xs, AGENT), 1):
        label = text(ax, x, 114, verb, size=28, bold=True)
        left = x - (text_width(fig, label) + 46) / 2
        label.set_x(left + 46)
        marker(ax, left + 18, 114, n, r=18, color=BLUE if n < 5 else TEAL)
        for j, line in enumerate(lines):
            text(ax, x, 430 + 31 * j, line, size=23, color=BODY, ha='center')
    r0, eps = RH
    one, two, three, four, five, six, seven, eight = xs

    scene = rhodium_face((5, 6, 3))
    ball_and_stick(scene, *st.water_box((-6.3, -6.5, 2.3), (6.3, 6.5, 8.6), seed=3))
    shot(ax, scene, front_view(32), (one - 96, 150, 192, 242), 11, centre=(0, 0, 2.2), background=TINT)

    page(ax, two - 76, 168, 112, 148)
    page(ax, two - 30, 208, 112, 148, chart=True)

    px = sketch(ax, (three - 80, 176, 160, 176), [(r0, eps, dict(color=INK, lw=pt(4)))])
    ax.plot(*np.transpose([px(r0, -9.5), px(r0, -eps)]), color=MUTED, lw=pt(2), ls=(0, (2, 2)), zorder=3)
    text(ax, *(px(r0, -9.5) + (0, 20)), 'r₀', size=24, bold=True, ha='center')
    arrow(ax, px(r0 + 0.75, 0), px(r0 + 0.75, -eps), color=INK, width=2.5, head=12, style='<|-|>')
    text(ax, *(px(r0 + 0.75, -eps / 2) + (12, 0)), 'ε', size=26, bold=True)

    scene = rt.Scene()
    a = st.LATTICE['Rh']
    for p in itertools.product((0, 0.5, 1), repeat=3):
        if sum(c == 0.5 for c in p) in (0, 2):  # the corners and face centres of the fcc cube
            scene.sphere(a * (np.array(p) - 0.5), 0.72, RH_COLOR)
    for p in itertools.product((0, 1), repeat=3):
        for axis in range(3):
            if not p[axis]:
                q = np.array(p)
                q[axis] = 1
                scene.cylinder(a * (np.array(p) - 0.5), a * (q - 0.5), 0.05, MUTED)
    shot(ax, scene, CRYSTAL_VIEWS['cube'], (four - 98, 150, 196, 242), 24, centre=(0, 0, 0), background=TINT)

    px = sketch(ax, (five - 80, 176, 160, 176), [(3.3, 4.0, dict(color=LINE, lw=pt(3.5), ls=(0, (2, 2)))),
                                                (r0, eps, dict(color=RH_COLOR, lw=pt(4.5)))])
    arrow(ax, px(3.3, -4.0) + (0, 10), px(r0, -eps) + (8, -6), color=MUTED, width=2.5, head=12, rad=-0.35)
    ax.add_patch(Circle(px(r0, -eps), 8, fc=RH_COLOR, ec='white', lw=pt(2.5), zorder=6))

    for j, (value, name, color) in enumerate(((209, 'IFF', RH_COLOR), (379, 'measured', INK))):
        x, height = six - 40 + 80 * j, 0.44 * value
        ax.add_patch(Rectangle((x - 26, 360 - height), 52, height, color=color, zorder=4))
        text(ax, x, 360 - height - 18, str(value), size=24, bold=True, color=color, ha='center')
        text(ax, x, 382, name, size=20, color=MUTED, ha='center')
    ax.plot([six - 82, six + 82], [360, 360], color=MUTED, lw=pt(2), zorder=5)

    page(ax, seven - 94, 208, 86, 112)
    arrow(ax, (seven, 264), (seven + 26, 264), color=MUTED, width=3, head=14)
    badge(ax, seven + 58, 250, 28, TEAL)
    text(ax, seven + 58, 304, '−7.84', size=26, bold=True, color=TEAL, ha='center')

    shot(ax, rhodium_face((5, 4, 2)), front_view(32), (eight - 104, 178, 132, 110), 7.6, centre=(0, 0, -1),
         background=TINT)
    badge(ax, eight + 54, 228, 24, TEAL)
    scene = rt.Scene()
    for end in (-2.4, 2.4):
        scene.sphere((end, 0, 0), 0.9, RH_COLOR)
    spring(scene, (-2.4, 0, 0), (2.4, 0, 0), INK, turns=5, radius=0.35, wire=0.07, inset=(0.9, 0.9))
    shot(ax, scene, FLAT, (eight - 104, 312, 132, 64), 17, centre=(0, 0, 0), background=TINT)
    flag(ax, eight + 46, 372, 56, ACCENT)
    result(fig, ax, 'Every number', ' comes from rhodium’s published values, and nothing here is a new fit or result',
           MUTED)
    return save(fig, 'agent')


def closing():
    """The cover's S7 on Pt(111) in water again, its phenylalanine ring marked: the closing bookend."""
    return s7_on_platinum('closing', ring=True)


FIGURES = (agent, closing)
