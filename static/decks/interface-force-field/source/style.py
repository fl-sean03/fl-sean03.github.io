"""The deck's palette and element colours, and where its files live; shared by the figures, the science checks and
the slide builder."""
from pathlib import Path

SOURCE = Path(__file__).resolve().parent
ASSETS = SOURCE.parent / 'assets'
DATA = SOURCE / 'data'

INK, BODY, MUTED = '#15191F', '#2E3440', '#5C6573'
RULE, LINE, TINT = '#E3E6EB', '#C5CBD3', '#F4F5F7'
ACCENT, ACCENT_SOFT = '#B3263E', '#F8E9EC'
BLUE, BLUE_SOFT = '#3474B8', '#E8F0F9'
TEAL = '#1D7F79'

# Slide px: the side of the square animation that shares slide 2's figure row, and the gap between them.
ANIMATION, GUTTER = 540, 28

# Element colour and ball radius (Å) for ball-and-stick pictures; metals use touching spheres.
ELEMENTS = {
    'H': ('#F3F4F6', 0.24), 'C': ('#59616E', 0.36), 'N': ('#3474B8', 0.36), 'O': ('#D9483B', 0.36),
    'Na': ('#8E63C7', 0.95), 'Cl': ('#52A447', 1.10), 'Si': ('#E7BE73', 0.42), 'P': ('#F0963A', 0.44),
    'Ca': ('#5FA46E', 0.62), 'Pt': ('#AEB6C1', 1.39), 'Au': ('#E2B23E', 1.44), 'Rh': ('#2C8C85', 1.34),
}
