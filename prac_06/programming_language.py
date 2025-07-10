"""CP1404/CP5632 Practical
programming language Time Estimate:
Estimate: 60 minutes
Actual:  120 minutes
"""

class ProgrammingLanguage:

    def __init__(self, name='', typing = '',  reflection =  False, year = 0):
        """Programming language class definition for programming languages."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """"Determine if language is dynamic."""
        if self.reflection:
            return True
        else:
            return False

    def __str__(self):
        """Display programming language information."""
        return f"{self.name},  { self.typing} Typing, Reflection={self.is_dynamic()} First appeared in {self.year}"

