#!/usr/bin/env python3
"""Sort translation lists alphabetically."""

import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"

FILES = {
    "custom": DATA_DIR / "words_custom.txt",
    "excluded": DATA_DIR / "words_excluded.txt",
}


def sort_file(filepath: Path) -> None:
    """Sort a text file alphabetically, preserving comments."""
    lines = filepath.read_text(encoding="utf-8").splitlines()

    comments = []
    entries = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            comments.append(stripped)
        elif stripped:
            entries.append(stripped)

    entries.sort(key=lambda x: x.lower())

    with open(filepath, "w", encoding="utf-8") as f:
        for comment in comments:
            f.write(comment + "\n")
        if comments:
            f.write("\n")
        for entry in entries:
            f.write(entry + "\n")


def main() -> None:
    args = sys.argv[1:]

    if not args:
        targets = FILES.values()
    elif args[0] == "custom":
        targets = [FILES["custom"]]
    elif args[0] == "excluded":
        targets = [FILES["excluded"]]
    else:
        print(f"Unknown argument: {args[0]}")
        print("Usage: python sort_lists.py [custom|excluded]")
        sys.exit(1)

    for filepath in targets:
        sort_file(filepath)
        print(f"Sorted: {filepath.name}")


if __name__ == "__main__":
    main()
