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
    guitars = load_guitars()
    display_guitars(guitars)

def display_guitars(guitars):
    """Display specific Guitar output for max_name_length value."""
    print("Printing guitars...")
    print("Sorting guitars by year...")
    guitars.sort()
    for guitar in guitars:
        print(guitar)

def load_guitars():
    guitars = []
    Guitar_fields = namedtuple("Guitar_fields", 'name, year, price')
    print("Loading guitars...")
    with open(FILENAME, "r", encoding='utf-8-sig') as in_file:
        for guitar_map_record in map(Guitar_fields._make, csv.reader(in_file)):
            # print(guitar_map_record.name, guitar_map_record.year, guitar_map_record.price)
            guitars.append(Guitar(guitar_map_record.name, int(guitar_map_record.year), float(guitar_map_record.price)))
        print("Successfully loaded guitars...")
        return guitars

main()

# for line in in_file:
#     print(line.strip())
# for guitar in csv.reader(in_file, delimiter=',', quotechar='"'):
#      print(guitar)