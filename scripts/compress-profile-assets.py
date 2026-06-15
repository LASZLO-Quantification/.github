from pathlib import Path
from PIL import Image

vault = Path(r"e:\Obsidian Vault\attachments\LASZLO")
out = Path(__file__).resolve().parents[1] / "profile" / "assets"
out.mkdir(parents=True, exist_ok=True)

banner_src = vault / "LASZLO_Logo_横版_深色底.png"
mark_src = vault / "LASZLO_Logo_标章_256.png"
term_src = vault / "LASZLO_UI_Terminal_终端.png"

img = Image.open(banner_src).convert("RGB")
w = 680
h = int(img.height * w / img.width)
img = img.resize((w, h), Image.LANCZOS)
banner = out / "laszlo-banner.jpg"
img.save(banner, format="JPEG", quality=80, optimize=True, progressive=True)

mark = Image.open(mark_src).convert("RGBA")
mark = mark.resize((128, 128), Image.LANCZOS)
mark_path = out / "laszlo-mark.png"
mark.save(mark_path, format="PNG", optimize=True)

term = Image.open(term_src).convert("RGB")
tw = 720
th = int(term.height * tw / term.width)
term = term.resize((tw, th), Image.LANCZOS)
term_path = out / "laszlo-terminal.jpg"
term.save(term_path, format="JPEG", quality=78, optimize=True, progressive=True)

for p in (banner, mark_path, term_path):
    print(p.name, p.stat().st_size)
