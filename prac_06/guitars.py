"""CP1404/CP5632 Practical
guitar Time Estimate:
Estimate: 120 minutes
Actual:  150 minutes
"""

from prac_06.guitar import Guitar

def main():
    """User inputs guitars and then prints guitars in formated string."""
    guitars = []
    new_guitars = add_guitar(guitars)
    display_guitars(new_guitars)


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
        print(f"{new_guitar.name} ({new_guitar.year}) : ${new_guitar.cost:,.2f} added")
        name = input("Name: ")
    return guitars

def display_guitars(guitars):
        """Display added guitars using display_guitars()."""
        print()
        print("These are my guitars:")
        max_name_length = max({len(guitar.name) for guitar in guitars})
        for count, guitar in enumerate(guitars):
            if guitar.is_vintage():
                print(f"Guitar {count + 1}: {guitar.display_guitar(max_name_length)} (vintage)")
            else:
                print(f"Guitar {count + 1}: {guitar.display_guitar(max_name_length)}")

main()

