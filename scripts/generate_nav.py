import os
from pathlib import Path

docs_dir = Path("docs")
nav_entries = ["- Home: index.md"]

for path in sorted(docs_dir.rglob("*.md")):
    if path.name == "index.md":
        continue
    relative_path = path.relative_to(docs_dir)
    title = path.stem.replace("-", " ").title()
    nav_entries.append(f"- {title}: {relative_path}")

with open("SUMMARY.txt", "w") as nav_file:
    nav_file.write("\n".join(nav_entries))
