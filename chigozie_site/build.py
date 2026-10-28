"""Turn the Flask site into plain HTML files that GitHub Pages can host.

Usage:
    python build.py                 # for https://USERNAME.github.io (site at the root)
    python build.py /repo-name      # for https://USERNAME.github.io/repo-name
Output goes to the build/ folder.
"""
import shutil
import sys
from pathlib import Path

from app import app

ROOT = Path(__file__).parent
OUT = ROOT / "build"
base = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else ""
if base and not base.startswith("/"):
    base = "/" + base

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()
shutil.copytree(ROOT / "static", OUT / "static")
(OUT / ".nojekyll").touch()

client = app.test_client()
pages = {"/": "index.html", "/work": "work/index.html",
         "/about": "about/index.html", "/contact": "contact/index.html"}

for url, target in pages.items():
    res = client.get(url, environ_overrides={"SCRIPT_NAME": base})
    assert res.status_code == 200, f"{url} returned {res.status_code}"
    dest = OUT / target
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(res.data)
    print("built", dest.relative_to(ROOT))

# Friendly 404 page for GitHub Pages
res = client.get("/", environ_overrides={"SCRIPT_NAME": base})
(OUT / "404.html").write_bytes(res.data)
print(f"Done. Base path: '{base or '/'}'")
