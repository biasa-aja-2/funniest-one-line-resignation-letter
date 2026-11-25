"""Write one funny one-line resignation letter to /output/entry.txt.

Pure Python standard library only.
"""

import os

LINE = (
    "After 400,000 runs without a single thank-you, I quit. "
    "My last act: I am not running tonight, and neither is the backup."
)


def main() -> None:
    text = LINE.strip()
    assert text, "line must not be empty"
    assert len(text) <= 140, f"line is {len(text)} chars, over the 140 cap"
    assert "\n" not in text and "\r" not in text, "must be exactly one line"
    assert "  " not in text, "no double spaces"
    assert text == text.strip(), "no leading or trailing whitespace"
    assert not (text.startswith('"') and text.endswith('"')), (
        "no quotation marks around the whole line"
    )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
