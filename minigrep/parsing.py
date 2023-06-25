"""This module supports the argument parsing of the minigrep CLI tool."""
import os.path

from typing import Tuple


class MinigrepParser:
    """Parse the arguments from the terminal."""

    def __init__(self, file: str, pattern: str, option: str):
        self.file_name = file
        self.pattern = pattern
        self.option = option

    def is_valid(self) -> bool:
        """Return true if the arguments are valid."""
        if not os.path.exists(self.file_name):
            print(f"The {self.file_name} file does not exist.")
            return False

        if not isinstance(self.pattern, str):
            print(f"The {self.pattern} argumentum is not a string.")
            return False

        if self.option not in ("-i", "--ignore-case", ""):
            print(f"The {self.option} is unknown.")
            return False

        return True

    def parse(self) -> Tuple[str, str, bool]:
        """Parse the terminal arguments."""
        content = ""
        with open(self.file_name, encoding="utf-8") as file:
            content = file.read()

        ignore_case = False
        if self.option in ("-i", "--ignore-case"):
            ignore_case = True

        return (self.pattern, content, ignore_case)
