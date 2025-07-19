"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""
    #modification 2.
    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        #modification 2.
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        """Return a string representation of the programming language."""
        #modification 3.
        return f"str: {self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}, pointer_arithmetic={self.pointer_arithmetic}"

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        #modification 2.
        return f"repr: {self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}, pointer_arithmetic={self.pointer_arithmetic}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"



def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    #modification 2
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)
    #modification 1
    c_plus_plus = ProgrammingLanguage("C++", "Static", False, 1983, True)

    languages = [ruby, python, visual_basic, c_plus_plus]
    print(python)
    #Test of modification 1 and 2
    print(c_plus_plus)
    print(repr(c_plus_plus))

    print()
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

    # Test of modification 1 and 2
    print()
    print("The pointer arithmetic languages are:")
    for language in languages:
        if language.pointer_arithmetic:
            print(language.name)


if __name__ == "__main__":
    run_tests()
