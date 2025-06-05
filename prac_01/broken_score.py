"""
CP1404/CP5632 - Practical
Someone was trying to write a program to tell the user if their score is invalid, bad, passable or excellent, but their code doesn't work.

Rewrite the following program using the most efficient if, elif, else structure you can. The code is available here at: broken_score.py
Remember to click Raw before copying and pasting so that you get proper formatting!

The intention is that the score must be between 0 and 100 inclusive; 90 or more is excellent; 50 or more is a pass; below 50 is bad. There is no intention to do any repetition.
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score < 50:
    print("Bad score")
elif 90 > score >= 50:
    print("Passable")
else:
    print("Excellent")


