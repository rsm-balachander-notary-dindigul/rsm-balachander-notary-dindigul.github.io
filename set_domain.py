from pathlib import Path
import sys
if len(sys.argv) != 2:
    print("Usage: python set_domain.py https://your-domain.example/path")
    raise SystemExit(1)
root = Path(__file__).parent
domain = sys.argv[1].rstrip("/")
p = root / "sitemap-template.xml"
text = p.read_text(encoding="utf-8").replace("https://YOUR-DOMAIN", domain)
(root/"sitemap.xml").write_text(text, encoding="utf-8")
robots = (root/"robots.txt").read_text(encoding="utf-8").rstrip() + f"\nSitemap: {domain}/sitemap.xml\n"
(root/"robots.txt").write_text(robots, encoding="utf-8")
print("Created sitemap.xml and updated robots.txt for", domain)
