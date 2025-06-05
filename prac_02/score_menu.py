"""Prac 02 Do-From-scratch Exercise 01: Menu"""
from score import determine_result
from math import floor
MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""
def main():
    """Menu used to ascertain input score."""
    score = 0
    print(MENU)
    menu_choice = input("Enter your choice: ").lower()
    while menu_choice != "q":
        if menu_choice == "g":
            score = float(input("Enter your score: "))
            while score < 0 or score > 100:
                print("Please enter a valid score between 0 and 100 inclusive")
                score = float(input("Enter your score: "))
        elif menu_choice == "p":
            print(f"Result: {determine_result(score)}")
        elif menu_choice == "s":
            print('*' * floor(score))
        else:
            print("Invalid choice")
        print(MENU)
        menu_choice = input("Enter your choice: ").lower()
    print("Goodbye.")


main()


