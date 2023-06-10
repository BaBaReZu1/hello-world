def search(input: str, pattern: str) -> list:
    """Search the first word of a string given a pattern."""
    first_index = input.find(pattern)
    
    while input[first_index] != ' ' :
        first_index = first_index - 1

    list_of_words = input[first_index:].split()

    matched_word = []
    for element in list_of_words:
        if pattern in element:
            matched_word.append(element)
    
    return '\n'.join(matched_word)

def search_ignore_case(input: str, pattern: str) -> str:
    """Search the first word of a string given a pattern. It ignores capital letters."""
    return search(input.lower(), pattern.lower())

def search_ignore_case2(input: str, pattern: str) -> str:
    
    original_words = input.split()
    found_words = []

    for idx, element in enumerate(original_words):
        if pattern.lower() in element.lower():
            found_words.append(original_words[idx])

    return found_words


gerp_description = """
In Linux and Unix Systems Grep, short for “global regular expression print”, 
is a command used in searchING and matchiNg text files contained in the regular expressions."""

pattern = "InG"

found_words = search_ignore_case2(gerp_description, pattern)
print(found_words)