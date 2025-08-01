"""" Basic list operations: Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
The program should then output information about these numbers, as in the output below. ou can use the functions
 min, max, sum and len, and you can use the append method to add a number to a list."""

def main():
    """Number list creation and test using functions min, max, sum and len."""
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average number is {sum(numbers)/len(numbers)}")

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")
main()