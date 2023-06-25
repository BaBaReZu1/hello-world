import sys
import os.path


def find_indicies(content: str, pattern: str) -> list:
    """Return a list of indicies from the `content` string that contains the `pattern` string."""
    input_words = content.split()

    indicies = [idx for idx, word in enumerate(input_words) if pattern in word]

    return indicies


def search(content: str, pattern: str, ignore_case: bool = False) -> list:
    """Return a list of words from `content` string that contains the `pattern` string. It ignores capital letters."""
    if ignore_case:
        content = content.lower()
        pattern = pattern.lower()

    indicies = find_indicies(content, pattern)
    words = content.split()

    found_words = [words[index] for index in indicies]

    return found_words


def read_arguments(arguments: list) -> tuple:
    """Read the content of the file last argument"""
    file = arguments[-1]
    pattern = arguments[-2]

    file_content = ""
    with open(file, encoding="utf-8") as file:
        file_content = file.read()

    return file_content, pattern


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 minigrep.py [OPTION] PATTERNS FILE")
        print("Example: `python3 minigrep.py -i 'and' grep.txt`")
        print("Use `python3 minigrep.py --help` for more details.")
        sys.exit()

    if sys.argv[1] == "--help":
        print("Usage: python3 minigrep.py [OPTION] PATTERNS FILE")
        print("Example: `python3 minigrep.py -i 'and' grep.txt`")
        print()
        print("Options:")
        print("\t -i, --ignore-case\t ignore capital letters")
        print("Report bugs at <https://github.com/BaBaReZu1/hello-world>")

    file_name = sys.argv[-1]
    if not os.path.exists(file_name):
        print(f"The {0} file does not exist. Please create the file.", file_name)

    content, pattern = read_arguments(sys.argv)

    found_words = []
    if len(sys.argv) == 3:
        found_words = search(content, pattern)
    elif sys.argv[1] == "-i" or sys.argv[1] == "--ignore-case":
        found_words = search(content, pattern, True)

    print(found_words)
