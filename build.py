"""Baut index.html (vollständige Seite fürs iPhone) aus src/app.html."""
from pathlib import Path

root = Path(__file__).parent
body = (root / "src" / "app.html").read_text(encoding="utf-8")

head = """<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Fener Sim">
<meta name="theme-color" content="#0b1838">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="manifest" href="manifest.webmanifest">
<style>
:root { padding-top: env(safe-area-inset-top, 0px); padding-bottom: 0; }
body { margin: 0; }
[hidden] { display: none !important; }
img { max-width: 100%; }
</style>
</head>
<body>
"""
(root / "index.html").write_text(head + body + "\n</body>\n</html>\n", encoding="utf-8")
print("index.html gebaut")
