"""Write the one-line joke entry to /output/entry.txt."""

import os

ENTRY = "The meeting's only decision was to schedule another meeting about the email the meeting was about."


def main() -> None:
    # The gate requires 1-200 characters, a single line, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY and ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
