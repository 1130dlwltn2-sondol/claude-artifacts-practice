#!/usr/bin/env python3
"""manuscript_full.md와 pages/를 조립한다."""
import shutil
from pathlib import Path

ROOT = Path.home() / "workspace" / "claude-artifacts-practice"
CHAPTERS = ROOT / "chapters"
PAGES = ROOT / "pages"

# pages/에 들어갈 순서: (pages 파일명, 원본 경로)
ORDER = [
    ("00-first-page.md", PAGES / "00-first-page.md"),
    ("01-copyright.md", PAGES / "01-copyright.md"),
    ("02-foreword.md", PAGES / "02-foreword.md"),
    ("03-prep.md", PAGES / "03-prep.md"),
    ("04-table-of-contents.md", PAGES / "04-table-of-contents.md"),
    ("10-chapter-1.md", CHAPTERS / "01.md"),
    ("20-chapter-2.md", CHAPTERS / "02.md"),
    ("30-chapter-3.md", CHAPTERS / "03.md"),
    ("40-chapter-4.md", CHAPTERS / "04.md"),
    ("50-chapter-5.md", CHAPTERS / "05.md"),
    ("60-chapter-6.md", CHAPTERS / "06.md"),
    ("70-chapter-7.md", CHAPTERS / "07.md"),
    ("80-chapter-8.md", CHAPTERS / "08.md"),
    ("90-final-project.md", PAGES / "90-final-project.md"),
    ("92-glossary.md", PAGES / "92-glossary.md"),
    ("93-sources.md", PAGES / "93-sources.md"),
    ("94-closing.md", PAGES / "94-closing.md"),
]

# 기존 pages/ 정리 후 재구성
tmp = {}
for name, src in ORDER:
    if not src.exists():
        raise SystemExit(f"missing: {src}")
    tmp[name] = src.read_text(encoding="utf-8")

for p in PAGES.glob("*.md"):
    p.unlink()
for name, text in tmp.items():
    (PAGES / name).write_text(text, encoding="utf-8")

# manuscript_full.md 조립 (이미지 경로는 루트 기준 assets/로)
parts = []
for name, _ in ORDER:
    text = (PAGES / name).read_text(encoding="utf-8")
    text = text.replace("../assets/", "assets/")
    parts.append(text.strip())

header = """# Claude로 문서·슬라이드·대시보드 만들기

무료로 시작하는 문서 제작부터 유료 베타 기능의 이해까지

저자: 이준수

---

"""
(ROOT / "manuscript_full.md").write_text(
    header + "\n\n---\n\n".join(parts) + "\n", encoding="utf-8"
)

print("pages:", len(list(PAGES.glob('*.md'))), "files")
print("manuscript_full.md:", (ROOT / "manuscript_full.md").stat().st_size, "bytes")
