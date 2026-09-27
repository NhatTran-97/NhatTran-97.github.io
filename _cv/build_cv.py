#!/usr/bin/env python3
"""Generate the LaTeX CV (_cv/cv.tex) from the website data files.

Reads _data/profile.yml, _data/cv.yml and _data/publications.yml, so the PDF
always matches the website. Compile with:  cd _cv && latexmk -xelatex cv.tex
(GitHub Actions does this automatically — see .github/workflows/cv-pdf.yml).
"""
import datetime
import pathlib
import re

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "_data"
OUT = ROOT / "_cv" / "cv.tex"

# Contacts whose value still looks like a template placeholder are left out of the PDF.
PLACEHOLDER = re.compile(r"XXXX|your-id|example\.com", re.I)


def load(name):
    with open(DATA / f"{name}.yml", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def esc(text):
    """Escape LaTeX special characters in plain text."""
    rep = {
        "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
        "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }
    return "".join(rep.get(c, c) for c in str(text))


def md(text):
    """Convert the small Markdown subset used in the data files to LaTeX."""
    text = str(text).strip()
    links = []

    def keep_link(m):
        links.append((m.group(1), m.group(2)))
        return f"\x00{len(links) - 1}\x00"

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", keep_link, text)
    text = esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"\\textit{\1}", text)
    text = re.sub(r"`(.+?)`", r"\\texttt{\1}", text)

    def put_link(m):
        label, url = links[int(m.group(1))]
        return r"\href{%s}{%s}" % (url.replace("%", r"\%").replace("#", r"\#"), md(label))

    return re.sub(r"\x00(\d+)\x00", put_link, text)


def bold_names(authors, names):
    out = esc(authors)
    for n in sorted(names or [], key=len, reverse=True):
        e = esc(n)
        # bold each name once, without re-bolding a shorter alias inside a longer one
        out = re.sub(r"(?<![\w{])" + re.escape(e) + r"(?![\w}])", r"\\textbf{" + e + "}", out, count=1)
    return out


def section_timeline(sec):
    lines = [r"\cvsection{%s}" % esc(sec["title"])]
    for it in sec.get("items") or []:
        lines.append(r"\cventry{%s}{%s}{%s}" % (
            md(it.get("title", "")), esc(it.get("period", "")), md(it.get("org", ""))))
        details = it.get("details") or []
        if details:
            lines.append(r"\begin{cvitems}")
            lines += [r"\item " + md(d) for d in details]
            lines.append(r"\end{cvitems}")
    return lines


def section_skills(sec):
    lines = [r"\cvsection{%s}" % esc(sec["title"]), r"\begin{cvskills}"]
    for g in sec.get("items") or []:
        lines.append(r"\cvskill{%s}{%s}" % (esc(g["group"]), esc(", ".join(map(str, g["items"])))))
    lines.append(r"\end{cvskills}")
    return lines


def section_publications(pubs, names):
    if not pubs:
        return []
    lines = [r"\cvsection{Publications}", r"\begin{cvpubs}"]
    for p in sorted(pubs, key=lambda p: -int(p.get("year", 0))):
        venue, year, note = str(p.get("venue", "")), str(p.get("year", "")), str(p.get("note") or "")
        where = venue if year in venue else f"{venue}, {year}"          # avoid "2026, 2026"
        tag = "" if not note or note.lower() in venue.lower() else r" \textcolor{accent}{\textbf{[%s]}}" % esc(note)
        lines.append(r"\item %s. \textit{%s}. %s.%s" % (
            bold_names(p.get("authors", ""), names), md(p.get("title", "")), esc(where), tag))
    lines.append(r"\end{cvpubs}")
    return lines


def main():
    profile, cv, pubs = load("profile"), load("cv"), load("publications")
    site = yaml.safe_load(open(ROOT / "_config.yml", encoding="utf-8"))

    contacts = []
    for c in profile.get("contacts") or []:
        value, url = str(c.get("value", "")), c.get("url")
        if PLACEHOLDER.search(value) or (url and PLACEHOLDER.search(url)):
            continue
        contacts.append(r"\href{%s}{%s}" % (url.replace("%", r"\%"), esc(value)) if url else esc(value))
    if site.get("url"):
        web = site["url"].replace("https://", "").rstrip("/")
        contacts.append(r"\href{%s}{%s}" % (site["url"], esc(web)))

    body = [
        r"\cvheader{%s}{%s}{%s}" % (esc(profile.get("name", "")), esc(profile.get("role", "")),
                                   r" \quad\textbullet\quad ".join(contacts)),
    ]
    summary = (profile.get("about") or {}).get("summary")
    if summary:
        body += [r"\cvsection{Summary}", md(summary)]

    for sec in cv.get("sections") or []:
        body += section_skills(sec) if sec.get("type") == "skills" else section_timeline(sec)
        if sec.get("id") == "experience":
            body += section_publications(pubs, profile.get("publication_names"))

    template = (ROOT / "_cv" / "template.tex").read_text(encoding="utf-8")
    tex = template.replace("%%BODY%%", "\n".join(body)).replace(
        "%%UPDATED%%", datetime.date.today().strftime("%B %Y"))
    OUT.write_text(tex, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
