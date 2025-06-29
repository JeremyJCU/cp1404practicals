"""CP1404/CP5632 Practical
programming language Time Estimate:
Estimate: 60 minutes
Actual: 120  minutes
"""

from prac_06.programming_language import ProgrammingLanguage

def main():
    """Use programming_language object to test print and field functionality"""
    python = ProgrammingLanguage('Python',"Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    c_plus = ProgrammingLanguage("C++", "Static", False, 1983)
    print(python)
    print(ruby)
    print(visual_basic)
    print(c_plus)
    print()
    programming_languages = [python, ruby, visual_basic, c_plus]
    print_dynamic(programming_languages)

def print_dynamic(programming_languages):
    """Display which programming languages are dynamic"""
    print("The dynamic typed languages are:")
    for programming_language in programming_languages:
        if programming_language.is_dynamic():
            print(programming_language.name)


main()