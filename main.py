#!/usr/bin/env python3
"""Write the best summary of Wednesday 11 November 2026's world news.

make.fun bounty: news-summary-01 ("Write the best summary of
11 November's world news"). The program is fully offline and
deterministic: it writes a fixed, researched summary to
/output/entry.txt. Running it twice produces byte-identical output.

Python 3.13, standard library only.
"""

import os
import tempfile

SUMMARY = 'Wednesday 11 November 2026\n\nThe wars dominated the day, but the talking may have mattered more than the fighting. President Donald Trump declared the war with Iran "militarily effectively over" after meeting Qatar\'s prime minister, and Secretary of State Marco Rubio said US economic pressure had worked well enough that "there\'s really no need for major combat operations any longer" — though both warned force remained possible. The Justice Department charged three alleged Iran-backed operatives over nearly 20 plots in the US and Europe, including a planned attack on RAF Fairford, and Treasury Secretary Scott Bessent was moved to a military base after threats on his life. Iran, whose Strait of Hormuz has been shut over 250 days, said it would "never return" to its pre-war status.\n\nIn Abu Dhabi, the first US-brokered Ukraine-Russia talks since February ended without a ceasefire but with agreement on a large prisoner swap, described by US envoy Jared Kushner as the biggest of the war. NATO jets were scrambled after drones strayed into Baltic airspace. In Gaza, Israeli strikes killed at least eight people, including a father and his 13-year-old son, as the ceasefire frayed; Israel\'s newly sworn-in parliament has no government after a deadlocked election.\n\nAt COP31 in Antalya, UN chief António Guterres told 102 world leaders it was "make or bake time", warning the planet is heading for more than 2.5°C of warming even if current pledges are kept, and proposed a climate justice compact funded in part by taxes on oil companies.\n\nIn Washington, October consumer prices rose 0.4%, hotter than expected, reviving December rate-rise talk, and House Republicans blocked an effort to impeach Defense Secretary Pete Hegseth, 211-204. China\'s trade surplus passed $1 trillion in ten months, a record pace, and Anthropic was reported to be seeking up to $3.5 billion in an IPO valuing it at about $1 trillion. In football, OL Lyonnes beat Juventus 6-0 in the Women\'s Champions League.\n'

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Write atomically (temp file + rename) so a failed run can never
    # leave a partial entry behind, then read the file back and verify
    # it meets the competition's rules: UTF-8, 1-2000 characters.
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=directory or ".", prefix=".entry-")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(SUMMARY)
        os.replace(tmp_path, OUTPUT_PATH)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != SUMMARY:
        raise SystemExit("entry.txt does not match the summary")
    if not 1 <= len(written) <= 2000:
        raise SystemExit(f"entry is {len(written)} characters, must be 1-2000")
    if not written.strip():
        raise SystemExit("entry is only white space")


if __name__ == "__main__":
    main()
