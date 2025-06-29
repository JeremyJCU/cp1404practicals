"""CP1404/CP5632 Practical
guitar Time Estimate:
Estimate: 120 minutes
Actual:  150 minutes
"""
from datetime import date

class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Set Guitar fields."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Output of Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f})"

    def display_guitar(self, max_name_length):
        """Display Guitar output with max_name_length value."""
        return f"{self.name:{max_name_length}} ({self.year}) : ${self.cost:,.2f})"

    def get_age(self):
        """Return age in years."""
        return date.today().year - self.year

    def is_vintage(self):
        """Return True if Guitar is vintage."""
        if self.get_age() >= 50:
            return True
        else:
            return False

