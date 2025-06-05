"""
CP1404/CP5632 - Practical
Someone was trying to write a program to tell the user if their score is invalid, bad, passable or excellent, but their code doesn't work.

Rewrite the following program using the most efficient if, elif, else structure you can. The code is available here at: score.py
Remember to click Raw before copying and pasting so that you get proper formatting!

The intention is that the score must be between 0 and 100 inclusive; 90 or more is excellent; 50 or more is a pass; below 50 is bad. There is no intention to do any repetition.
"""
from random import randint

def main():
    """Take score and print determined result."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print("Human entered: ", result)
    random_score = float(randint(0, 100))
    result = determine_result(random_score)
    print(f"Computer generated result: {result} from score: {random_score} ")

def determine_result(score):
    """Determine score result."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad score"
    elif 90 > score >= 50:
        return "Passable"
    else:
        return "Excellent"

if __name__ == "main()":
    main()
