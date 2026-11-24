"""Entry for make.fun bounty u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.

Writes one single-sentence satirical roast to /output/entry.txt.
Standard library only; deterministic: the same line every run.

The roast: the committee writing the law that will govern artificial
intelligence cannot convert its own draft to PDF — the chairman printed
it, signed it in pen, and sent it back to be scanned in. Authority set
up first, undercut by the file at the end. 218 characters, one sentence,
inside the 1-320 gate.
"""

import os

LINE = (
    "The committee writing the law that will govern artificial "
    "intelligence spent its morning asking an intern to convert the "
    "draft to PDF, after the chairman printed it, signed it in pen, "
    "and sent it back to be scanned in."
)


def main():
    # Gate: 1-320 characters, one line, no trailing newline.
    if not 1 <= len(LINE) <= 320:
        raise ValueError("entry line must be 1-320 characters, got %d" % len(LINE))
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
