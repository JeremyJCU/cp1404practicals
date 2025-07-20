"""CP1404/CP5632 Practical
Project Management Program! :
Estimate: 255 19:38  minutes
Actual:   minutes
"""

import datetime
import uuid


class Project:

    def __init__(self, name="", start_date=None, priority=0, cost_estimate=0.0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage
        self.id = uuid.uuid4()

    def __str__(self):
        date = self.start_date.strftime("%d/%m/%Y")
        return f"{self.name}, start:{date}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%"

    def __repr__(self):
        """Display general Guitar information."""
        return f"{self.name},{self.start_date},{self.priority},{self.cost_estimate},{self.completion_percentage}, self.id: {self.id}"

    def __lt__(self, other):
        return self.priority < other.priority

def testing():
    date = datetime.datetime.strptime("30/08/1977", "%d/%m/%Y").date()
    p1 = Project("Build Car Park",date,2,	600000.0,	95)
    date = p1.start_date.strftime("%d/%m/%Y")
    print(date)
    # print(p1)

    # date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    # date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    # print(f"That day is/was {date.strftime('%A')}")
    # print(date.strftime("%d/%m/%Y/"))


if __name__ == "__main__":
    testing()
