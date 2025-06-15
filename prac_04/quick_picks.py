"""
CP1404/CP5632 - Practical
Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that many
lines of output. Each line consists of 6 random numbers between 1 and 45. These values should be stored as CONSTANTS.
Each line (quick pick) should not contain any repeated number.
Each line of numbers should be displayed in sorted (ascending) order.
Study the formatting below so that numbers align neatly.
"""
from random import randint

RANGE_START = 1
RANGE_END = 45
LINE_LENGTH = 6


def main():
    """Create quick picks lines and display them."""
    quick_pick_number = int(input("How many quick picks? "))
    quick_picks = generate_quick_picks(quick_pick_number)
    display_quick_picks(quick_picks)

def display_quick_picks(quick_picks):
    """Display formated quick picks."""
    for quick_pick in quick_picks:
        print(f"{quick_pick[0]:2} {quick_pick[1]:2} {quick_pick[2]:2} {quick_pick[3]} {quick_pick[4]} {quick_pick[5]}")

def generate_quick_picks(quick_pick_number):
    """Generate quick picks using user input and return as a nested list."""
    quick_picks = []
    for i in range(quick_pick_number):
        line_picks = []
        for i in range(LINE_LENGTH):
            pick = randint(RANGE_START, RANGE_END)
            while pick in line_picks:
                pick = randint(RANGE_START, RANGE_END)
            line_picks.append(pick)
        line_picks.sort()
        quick_picks.append(line_picks)
    return quick_picks


main()


