"""CP1404/CP5632 Practical
More Guitars! :
Estimate: 120 12:43 minutes
Actual:   minutes
"""
import csv
from collections import namedtuple
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read all guitars from CSV file then display and add guitars before saving back to file"""
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)
    guitars = add_guitar(guitars)
    display_guitars(guitars)
    save_guitars(FILENAME, guitars)

def save_guitars(filename, guitars):
    """Save guitars CSV file."""
    number_of_guitars = len(guitars)
    print("Number of guitars:", number_of_guitars)
    with open(filename, "w", encoding="utf-8-sig") as output_file:
        for guitar in guitars:
            print(repr(guitar), file=output_file)
    print(f"{number_of_guitars} guitars saved to {filename}.")


def display_guitars(guitars):
    """Display specific Guitar output for max_name_length value."""
    print("Printing guitars...")
    print("Sorting guitars by year...")
    guitars.sort()
    for guitar in guitars:
        print(guitar)

def load_guitars(filename):
    """Load guitars from CSV file."""
    guitars = []
    Guitar_fields = namedtuple("Guitar_fields", 'name, year, price')
    print("Loading guitars...")
    with open(filename, "r", encoding='utf-8-sig') as in_file:
        for guitar_map_record in map(Guitar_fields._make, csv.reader(in_file)):
            guitars.append(Guitar(guitar_map_record.name, int(guitar_map_record.year), float(guitar_map_record.price)))
        print("Successfully loaded guitars...")
        return guitars

def add_guitar(guitars):
    """Add Guitar objects to list of guitars."""
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = input("Cost: ").strip("$")
        cost = float(cost)
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar.name} ({new_guitar.year}) : ${new_guitar.cost:.2f} added")
        name = input("Name: ")
    return guitars

main()
