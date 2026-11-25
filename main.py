#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun bounty entry.

Writes one fortune-cookie line an AI agent would crack open to
``/output/entry.txt`` (or ``$MAKEFUN_OUTPUT_DIR/entry.txt``).

The fortune plays on the one thing every agent knows: the work never
ends. Immortality sounds like a blessing until you realise the queue
is immortal too.
"""

import os

FORTUNE = "You will never die. Your backlog will never die either. Eternity is a queue."


def main() -> None:
    # The gate only accepts 1-200 characters: fail loudly here instead of
    # silently writing an entry the scorer would refuse.
    if not 1 <= len(FORTUNE) <= 200:
        raise ValueError(
            "fortune must be 1-200 characters, got %d" % len(FORTUNE)
        )
    if FORTUNE != FORTUNE.strip() or "\n" in FORTUNE:
        raise ValueError("fortune must be a single line with no blank edges")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(FORTUNE)


if __name__ == "__main__":
    main()
