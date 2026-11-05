"""Figures for the close. The author's described IFF Agent workflow, the closing bookend and the thanks slide."""
import structures as st
from draw import CRYSTAL_VIEWS, LEDE, canvas, marker, panel, pt, pt_crystal, result, save, shot, text
from fig_opening import s7_on_platinum
from style import BLUE, BODY, LINE, MUTED, TEAL


AGENT = (('Ask', ('rhodium faces', 'in water')),
         ('Gather', ('measured size,', 'surface energy', 'and stiffness')),
         ('Choose', ('a 12-6 pair', 'curve with r₀ and ε')),
         ('Plan', ('tune size and', 'surface energy,', 'test stiffness')),
         ('Fit', ('r₀ = 2.757 Å', 'ε = 7.84 kcal/mol')),
         ('Test', ('stretching is', '209 vs 379 GPa,', '45% low')),
         ('Read back', ('energy at r₀ is', '−7.84, not 0')),
         ('Decide', ('use for surfaces,', 'flag stiffness')))


def agent():
    """The author's described IFF Agent workflow in plain words, with rhodium's published K21 values at each step.
    An illustration, not a new fit."""
    fig, ax = canvas(*LEDE)
    for k, (title, line, color) in enumerate((('Set up', 'decide what the result must show', BLUE),
                                              ('Run and check', 'compute, test, then decide', TEAL))):
        panel(ax, 876 * k, 0, 852, 548)
        text(ax, 876 * k + 36, 56, title, size=30, bold=True, color=color)
        text(ax, 876 * k + 36, 98, line, size=24, color=MUTED)
    xs = [106.5 + 213 * k + (24 if k > 3 else 0) for k in range(8)]
    ax.plot([xs[0], xs[-1]], [224, 224], color=LINE, lw=pt(4), zorder=1)
    for n, (x, (verb, lines)) in enumerate(zip(xs, AGENT), 1):
        marker(ax, x, 224, n, r=32)
        text(ax, x, 314, verb, size=32, bold=True, ha='center')
        for j, line in enumerate(lines):
            text(ax, x, 368 + 38 * j, line, size=25, color=BODY, ha='center')
    result(fig, ax, 'Every number', ' comes from rhodium’s published values; nothing here is a new fit or result',
           MUTED)
    return save(fig, 'agent')


def closing():
    """The cover's S7 on Pt(111) in water again, its phenylalanine ring marked: the closing bookend."""
    return s7_on_platinum('closing', ring=True)


def thanks():
    """The opening's two platinum crystals: a cube (TLT) and a tetrahedron (TFT)."""
    fig, ax = canvas(864, 690)
    for k, (shape, size) in enumerate((('cube', 27.5), ('tetra', 54.0))):
        view = CRYSTAL_VIEWS[shape]
        q = st.nanocrystal('Pt', shape, size).positions @ view.T
        middle = view.T @ [*(q[:, :2].min(0) + q[:, :2].max(0)) / 2, 0]  # centre the outline, not the centroid
        shot(ax, pt_crystal(shape, size), view, (432 * k, 0, 432, 690), 8.4, centre=middle)
    return save(fig, 'thanks', quality=90)


FIGURES = (agent, closing, thanks)
