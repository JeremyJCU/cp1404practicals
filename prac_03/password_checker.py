"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    length = len(password)
    print(f"length {length}")
    if MIN_LENGTH <= length <= MAX_LENGTH:
        is_valid_length = True
    else:
        is_valid_length = False

    print("is valid length", is_valid_length)
    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0


    for character in password:
        if character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character.isdigit():
            number_of_digit += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1
        else:
            return False

    print(f"lower: {number_of_lower} upper: {number_of_upper} digit: {number_of_digit} special: {number_of_special}")
    # print(f"IS_SPECIAL_CHARACTER_REQUIRED {IS_SPECIAL_CHARACTER_REQUIRED}")
    if not IS_SPECIAL_CHARACTER_REQUIRED:
        if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0 or not is_valid_length:
            return False
        else:
            return True
    else:
        if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0 or number_of_special == 0 or not is_valid_length:
            return False
        else:
            return True

main()