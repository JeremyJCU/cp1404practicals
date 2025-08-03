"""
CP1404/CP5632 Practical
taxi simulator program class
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = """Let's drive!
q)uit, c)hoose taxi, d)rive
"""

def main():
    """Menu logic for taxi simulation."""
    bill_to_date = 0
    current_taxi = None
    taxi_container = [Taxi("Prius 1", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            display_available_taxis(taxi_container)
            current_taxi = choose_taxi(len(taxi_container))
        elif choice == "d":
            if current_taxi is not None:
                bill_to_date +=  drive_taxi(taxi_container[current_taxi])
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid choice")
        print_bill(bill_to_date)
        print(MENU)
        choice = input(">>> ").lower()

def drive_taxi(selected_taxi):
    """Dive selected taxi."""
    distance = int(input("Drive how far?: "))
    selected_taxi.start_fare()
    selected_taxi.drive(distance)
    return selected_taxi.get_fare()


def display_available_taxis(taxi_container):
    """Create list of available taxis."""
    for num, taxi in enumerate(taxi_container):
        print(num + 1, taxi)

def choose_taxi(number_of_taxis):
    """Allow user to choose a valid taxi."""
    choice = int(input("Choose  taxi: "))
    if  choice > number_of_taxis or choice < 0:
        print("Invalid taxis choice")
        return None
    else:
        choice -= 1
        return choice

def print_bill(bill_to_date):
    """Display formatted bill."""
    print(f"Bill to date: ${bill_to_date:.2f}")



main()