import sys


def search_case(original: str, input: str, pattern: str) -> list:
    # TODO: Implement the same algorithm using the original input string
    pass

def search_case(input: str, pattern: str, ignore_case: bool = False) -> list:
    """Search the first word of a string given a pattern. It ignores capital letters."""
    original_words = input.split()
    found_words = []

    if ignore_case:
        pattern = pattern.lower()
        input = input.lower()

    for idx, element in enumerate(input.split()):
        if pattern in element:
            found_words.append(original_words[idx])

    return found_words

def search_incase(input: str, pattern: str) -> list:
    return search_case(input, pattern, True)

def read_file(file_name: str) -> str:
    with open(file_name, "r") as txt:
        content = txt.read()
    
    return content


if __name__ == '__main__':
    # TODO: Handle exceptions. Show help how to use program

    if 

    if len(sys.argv) == 3:
        pattern = sys.argv[1]
        file = sys.argv[2]
        content = read_file(file)
        
        found_words = search_case(content, pattern)

    elif sys.argv[1] == "-i" or sys.argv[1] == "--ignore-case":
        pattern = sys.argv[2]
        file = sys.argv[3]
        content = read_file(file)

        found_words = search_incase(content, pattern)
        
    print(found_words)