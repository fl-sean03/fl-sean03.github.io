"""Render the static PDF as PNG previews, SVG slides and light contact sheets."""
from pathlib import Path

import pymupdf as fitz
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
BG = "#FBFAF7"
CARD = "#F3F0E8"
TEXT = "#1B1B1A"
RULE = "#E3DFD6"


def contact_sheet(tiles, columns):
    rows = (len(tiles) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * 446, rows * 276), BG)
    for index, tile in enumerate(tiles):
        sheet.paste(tile, ((index % columns) * 446, (index // columns) * 276))
    return sheet


def render():
    output = ROOT / "build" / "rendered"
    slides = ROOT / "build" / "slides"
    output.mkdir(parents=True, exist_ok=True)
    slides.mkdir(parents=True, exist_ok=True)
    thumbs = []
    label_font = ImageFont.load_default(size=14)
    with fitz.open(ROOT / "build" / "iff-visual-showcase.pdf") as document:
        for index, page in enumerate(document):
            png = output / f"slide-{index + 1:02}.png"
            pixmap = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
            pixmap.save(png)
            (slides / f"{index + 1:02}.svg").write_text(page.get_svg_image())
            image = Image.open(png).convert("RGB")
            if index == 0:
                image.save(ROOT / "build" / "cover.png")
            image.thumbnail((426, 240))
            tile = Image.new("RGB", (446, 276), CARD)
            tile.paste(image, ((446 - image.width) // 2, 10))
            draw = ImageDraw.Draw(tile)
            draw.line((0, 275, 445, 275), fill=RULE)
            lines = page.get_text().splitlines()
            title = lines[2][:49] if len(lines) > 2 else ""
            draw.text((12, 252), f"{index + 1:02}  {title}", fill=TEXT, font=label_font)
            thumbs.append(tile)
        page_count = len(document)
    for offset in range(0, len(thumbs), 12):
        contact_sheet(thumbs[offset:offset + 12], 3).save(output / f"contact-{offset // 12 + 1}.png")
    contact_sheet(thumbs, 5).save(output / "contact-all.png")
    print(f"Rendered {page_count} pages as PNG and SVG")


if __name__ == "__main__":
    render()
