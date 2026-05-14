import qrcode
from pathlib import Path

APP_URL = "https://deine-domain.example/"
TRACKS = [
    # ("1974_ABBA_Waterloo", "spotify:track:3Dy4REq8O09IlgiwuHQ3sk"),
]

out = Path("qr_codes")
out.mkdir(exist_ok=True)

for name, uri in TRACKS:
    url = APP_URL + "?track=" + uri
    img = qrcode.make(url)
    img.save(out / f"{name}.png")
