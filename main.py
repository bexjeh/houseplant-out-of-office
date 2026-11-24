"""Houseplant out-of-office auto-reply.

Writes one out-of-office message, at most 120 characters, as if a
houseplant had written it, to ``entry.txt`` inside the directory named
by ``MAKEFUN_OUTPUT_DIR`` (the current directory when unset).

The message is fixed: no clock, no randomness, no network, so every
run writes exactly the same bytes.
"""

import os

MESSAGE = "Out of office. The cat ate my best leaf and my human wasn't even here to witness it. Send water, not condolences."
# 113 characters: inside the 1-120 gate with room to spare, and no
# trailing newline, so the file holds exactly this message.

MAX_CHARS = 120


def main() -> None:
    text = MESSAGE.strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit("entry text must be 1 to 120 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(path, encoding="utf-8", newline="") as handle:
        if handle.read() != text:
            raise SystemExit("entry.txt did not round-trip")  # pragma: no cover


if __name__ == "__main__":
    main()
