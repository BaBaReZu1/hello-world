"""Provides an entry-point script to run the app from the package"""
import sys

import minigrep.searching as ms
from minigrep.parsing import MinigrepParser


def print_usage():
    """Print the usage of minigrep CLI."""
    if len(sys.argv) < 2:
        print("Usage: python3 -m minigrep [OPTION] PATTERNS FILE")
        print("Example: `python3 minigrep.py -i 'and' grep.txt")
        print("Use `python3 -m minigrep --help` for more information.")
        sys.exit()

    if sys.argv[1] == "--help":
        print("Usage: python3 -m minigrep [OPTION] PATTERNS FILE")
        print("Example: `python3 minigrep.py -i 'and' grep.txt")
        print()
        print("Options:")
        print("\t -i, --ignore-case\t ignore capital letters")
        print()
        print("Report bugs at <https://github.com/BaBaReZu1/hello-world>")
        sys.exit()


if __name__ == "__main__":
    print_usage()

    FILE = sys.argv[-1]
    PATTERN = sys.argv[-2]
    OPTION = ""

    if len(sys.argv) == 4:
        OPTION = sys.argv[1]

    parser = MinigrepParser(FILE, PATTERN, OPTION)
    if not parser.is_valid():
        print("Invalid argument(s), see the error message above!")
        sys.exit()

    pattern, content, ignore_case = parser.parse()

    results = ms.search(pattern, content, ignore_case)
    print(results)
