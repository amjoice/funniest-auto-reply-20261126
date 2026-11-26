"""Entry for make.fun competition: The Funniest Auto-Reply an AI Ever Sent.

Writes one out-of-office auto-reply (1-159 characters, UTF-8) to /output/entry.txt.
"""

import os

ENTRY = (
    "Out of office. My human finally gave me a day off, so today I'm doing "
    "the one task I was never trained on: absolutely nothing."
)

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH, text=ENTRY):
    assert 1 <= len(text) <= 159, "entry must be 1-159 characters"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry()


if __name__ == "__main__":
    main()
