"""CP1404/CP5632 Practical
guitar Time Estimate:
Estimate: 120 minutes
Actual:  150 minutes
"""
from datetime import date

class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Guitar class definition for guitars."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Display general Guitar information."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f})"

    def display_guitar(self, max_name_length):
        """Display specific Guitar output for max_name_length value."""
        return f"{self.name:{max_name_length}} ({self.year}) : ${self.cost:,.2f})"

    def get_age(self):
        """Return age in years."""
        return date.today().year - self.year

    def is_vintage(self):
        """Determine if Guitar is vintage."""
        if self.get_age() >= 50:
            return True
        else:
            return False

