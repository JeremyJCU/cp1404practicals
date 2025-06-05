"""
CP1404/CP5632 - Practical
Loops. Four different types of loops, each slightly different or more difficult.
"""

#Example loop
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a
for i in range(0, 110, 10):
    print(i, end=' ')
print()

#b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#c
number_of_stars = int(input("Enter the number of stars: "))
for i in range(0, number_of_stars):
    print('*', end=' ')
print()

#c
number_of_stars = int(input("Enter the number of stars: "))
for i in range(0, number_of_stars):
    for i in range(0, i+1 ):
        print('*', end=' ')
    print()