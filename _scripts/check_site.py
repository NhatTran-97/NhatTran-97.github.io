#!/usr/bin/env python3
"""Check the website content for mistakes before (or after) publishing.

  python3 _scripts/check_site.py            # check data files, pages and posts
  python3 _scripts/check_site.py _site      # also check links/images in a built site

Errors (exit code 1) break the site; warnings are things to review.
Runs automatically on GitHub: .github/workflows/check-site.yml
"""
import pathlib
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors, warnings = [], []

# Lĩnh vực nên dùng (README mục 11) - khác danh sách này chỉ là cảnh báo
CATEGORIES = {"Embedded & Hardware", "Perception & AI", "Autonomy", "Teaching & Mentoring",
              "Tools & Tips", "Research"}
PLACEHOLDER = re.compile(r"XXXX|your-id|example\.com|your\.email", re.I)


def err(where, msg):
    errors.append(f"{where}: {msg}")


def warn(where, msg):
    warnings.append(f"{where}: {msg}")


def load_yaml(path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        mark = getattr(e, "problem_mark", None)
        line = f" (line {mark.line + 1})" if mark else ""
        err(path.relative_to(ROOT), f"YAML syntax error{line}: {getattr(e, 'problem', e)}"
            " - check indentation and put text containing ':' in quotes")
        return None


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        err(path.relative_to(ROOT), "missing front matter (the block between two '---' lines at the top)")
        return None
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        mark = getattr(e, "problem_mark", None)
        line = f" (line {mark.line + 2})" if mark else ""
        err(path.relative_to(ROOT), f"front matter YAML error{line}: {getattr(e, 'problem', e)}")
        return None


def icons():
    text = (ROOT / "_includes/icon.html").read_text(encoding="utf-8")
    return set(re.findall(r'when "([a-z0-9-]+)"', text))


ICONS = icons()


def check_icon(where, name):
    if name and name not in ICONS:
        err(where, f"unknown icon '{name}'. Available: {', '.join(sorted(ICONS))}")


def check_file(where, url, what="file"):
    """Local paths (/assets/...) must exist in the repository."""
    if not url or not isinstance(url, str) or not url.startswith("/") or url.startswith("//"):
        return
    path = unquote(urlparse(url).path)
    if path.startswith("/assets/") or path.startswith("/favicon"):
        if not (ROOT / path.lstrip("/")).exists():
            err(where, f"{what} not found: {url}")


def require(where, item, *keys):
    for k in keys:
        if item.get(k) in (None, ""):
            err(where, f"missing '{k}'")


# ----------------------------------------------------------------------------
def check_profile():
    p = load_yaml(ROOT / "_data/profile.yml")
    if p is None:
        return {}
    w = "_data/profile.yml"
    require(w, p, "name")
    check_file(w + " avatar", p.get("avatar"), "image")
    hero = p.get("hero") or {}
    check_file(w + " hero.background", hero.get("background"), "image")
    for b in hero.get("buttons") or []:
        check_icon(w + f" hero button '{b.get('text')}'", b.get("icon"))
        check_icon(w + f" hero button '{b.get('text')}'", b.get("icon_after"))
    for i, h in enumerate(p.get("highlights") or [], 1):
        ww = f"{w} highlights #{i}"
        require(ww, h, "title", "text")
        check_icon(ww, h.get("icon"))
        if len(str(h.get("text", ""))) > 65:
            warn(ww, f"text is {len(h['text'])} characters; keep it around 45-60 so it fits in 2 lines")
    for c in p.get("contacts") or []:
        ww = f"{w} contacts '{c.get('label')}'"
        require(ww, c, "icon", "value")
        check_icon(ww, c.get("icon"))
        if PLACEHOLDER.search(str(c.get("value", "")) + str(c.get("url", ""))):
            warn(ww, "still a placeholder link - put the real link or delete this contact")
    return p


def check_cv():
    cv = load_yaml(ROOT / "_data/cv.yml")
    if cv is None:
        return
    w = "_data/cv.yml"
    if cv.get("pdf"):
        check_file(w + " pdf", cv["pdf"])
    if cv.get("pdf_text_align") not in (None, "justify", "left"):
        err(w, "pdf_text_align must be 'justify' or 'left'")
    ids = set()
    for s in cv.get("sections") or []:
        ww = f"{w} section '{s.get('title')}'"
        require(ww, s, "id", "title")
        if s.get("id") in ids:
            err(ww, f"duplicate id '{s['id']}'")
        ids.add(s.get("id"))
        check_icon(ww, s.get("icon"))
        for it in s.get("items") or []:
            if s.get("type") == "skills":
                require(ww, it, "group", "items")
            else:
                require(ww, it, "title")
                if not isinstance(it.get("details", []), list):
                    err(ww + f" '{it.get('title')}'", "'details' must be a list (lines starting with '- ')")


def check_projects():
    d = load_yaml(ROOT / "_data/projects.yml")
    if d is None:
        return
    w = "_data/projects.yml"
    groups = {g.get("id") for g in d.get("groups") or []}
    for g in d.get("groups") or []:
        require(f"{w} group", g, "id", "title")
        check_icon(f"{w} group '{g.get('id')}'", g.get("icon"))
    titles = set()
    for it in d.get("items") or []:
        ww = f"{w} project '{it.get('title')}'"
        require(ww, it, "title", "group", "description")
        if it.get("title") in titles:
            err(ww, "duplicate title (cards and links use the title as an id)")
        titles.add(it.get("title"))
        if it.get("group") not in groups:
            err(ww, f"group '{it.get('group')}' is not defined in 'groups' ({', '.join(sorted(groups))})")
        if it.get("category") and it["category"] not in CATEGORIES:
            warn(ww, f"category '{it['category']}' is not one of the usual categories: {', '.join(sorted(CATEGORIES))}")
        check_file(ww + " image", it.get("image"), "image")
        if not isinstance(it.get("tags", []), list):
            err(ww, "'tags' must be a list, e.g. [ROS 2, C++]")
        detail = it.get("detail")
        if detail:
            m = re.fullmatch(r"/projects/([a-z0-9-]+)/", detail)
            if not m:
                err(ww, f"detail must look like /projects/<file-name>/ (got {detail})")
            elif not (ROOT / "_projects" / f"{m.group(1)}.md").exists():
                err(ww, f"detail page file _projects/{m.group(1)}.md does not exist")
        for l in it.get("links") or []:
            require(ww + " link", l, "name", "url")
            check_icon(ww + f" link '{l.get('name')}'", l.get("icon"))


def check_project_pages():
    unfinished = []
    for f in sorted((ROOT / "_projects").glob("*.md")):
        w = str(f.relative_to(ROOT))
        if not re.fullmatch(r"[a-z0-9-]+\.md", f.name):
            err(w, "file name must be lowercase letters, numbers and '-' only")
        fm = front_matter(f)
        if fm is None:
            continue
        require(w, fm, "title")
        check_file(w + " image", fm.get("image"), "image")
        for l in fm.get("links") or []:
            require(w + " link", l, "name", "url")
            check_icon(w + f" link '{l.get('name')}'", l.get("icon"))
        body = f.read_text(encoding="utf-8")
        for src in re.findall(r'(?:src="|\]\()(/assets/[^")\s]+)', body):
            check_file(w, src, "image")
        if "Details coming soon" in body:
            unfinished.append(f.stem)
    if unfinished:
        warn("_projects/", f"{len(unfinished)} page(s) still say 'Details coming soon': {', '.join(unfinished)}")


def check_publications(profile):
    pubs = load_yaml(ROOT / "_data/publications.yml")
    if pubs is None:
        return
    names = profile.get("publication_names") or []
    for p in pubs if isinstance(pubs, list) else []:
        w = f"_data/publications.yml '{str(p.get('title'))[:50]}'"
        require(w, p, "title", "authors", "venue", "year", "type")
        if p.get("year") and not str(p["year"]).isdigit():
            err(w, "year must be a number, e.g. 2026")
        if names and not any(n in str(p.get("authors", "")) for n in names):
            warn(w, "none of profile.yml publication_names appears in authors, so your name will not be bold")
        check_file(w + " pdf", p.get("pdf"))


def check_posts():
    for f in sorted((ROOT / "_posts").glob("*")):
        w = str(f.relative_to(ROOT))
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}-[a-z0-9-]+\.md", f.name):
            err(w, "post file name must be YYYY-MM-DD-title-in-lowercase.md")
        fm = front_matter(f)
        if fm is None:
            continue
        require(w, fm, "title")
        check_file(w + " image", fm.get("image"), "image")
        if fm.get("category") and fm["category"] not in CATEGORIES:
            warn(w, f"category '{fm['category']}' is not one of the usual categories")


# ----------------------------------------------------------------------------
class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for key in ("href", "src"):
            if a.get(key) and not (tag == "link" and a.get("rel") in ("preconnect", "dns-prefetch")):
                self.links.append(a[key])


def check_built_site(site):
    """Every internal link and image in the built HTML must point to a real file."""
    site = pathlib.Path(site)
    for page in site.rglob("*.html"):
        parser = LinkParser()
        parser.feed(page.read_text(encoding="utf-8", errors="replace"))
        for link in parser.links:
            u = urlparse(link)
            if u.scheme or link.startswith(("#", "mailto:", "data:", "//")):
                continue
            path = unquote(u.path)
            if not path:
                continue
            target = (site / path.lstrip("/")) if path.startswith("/") else (page.parent / path)
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                err(str(page.relative_to(site)), f"broken link: {link}")


def check_styles():
    """In .scss a '//' comment runs to the end of the line, so CSS written after it
    on the same line is silently dropped (e.g. 'a: 1;  // note  b: 2;' loses b)."""
    for f in sorted((ROOT / "_sass").rglob("*.scss")) + sorted((ROOT / "assets" / "css").glob("*.scss")):
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            code = re.sub(r'"[^"]*"|\'[^\']*\'|url\([^)]*\)', "", line)
            if "//" in code:
                before, comment = code.split("//", 1)
                if before.strip() and re.search(r"[a-z-]+\s*:\s*[^;]+;", comment):
                    err(f"{f.relative_to(ROOT)} line {n}",
                        "CSS after a '//' comment is ignored - move the comment to its own line")


def main():
    profile = check_profile()
    check_cv()
    check_projects()
    check_project_pages()
    check_publications(profile)
    check_posts()
    check_styles()
    if len(sys.argv) > 1:
        check_built_site(sys.argv[1])

    for w in warnings:
        print(f"WARNING  {w}")
    for e in errors:
        print(f"ERROR    {e}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
