#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it, to
/output/entry.txt.

The joke: the plant's inbox is as neglected as the plant itself. It has
not been watered since March, so the sender's email queues behind the
sun — the one thing the plant still gets on schedule. The punch lands
on the last words, where the queue turns out to be cosmic, not clerical.
"""

import os

ENTRY = "Out of office until someone waters me. Last watered: March. Your email is in line behind the sun."

def main():
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars, must be 1-120"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
