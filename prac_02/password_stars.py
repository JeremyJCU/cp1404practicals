"""Practical 02 password program"""
PASSWORD_LENGTH = 10
def main():
    """Get a password and display representation using star character"""
    password = get_password()
    display_password(password)


def display_password(password):
    """Display the password using star character"""
    print("*" * len(password))


def get_password():
    """Get a valid password from the user"""
    user_password = input("Enter your password: ")
    while len(user_password) < PASSWORD_LENGTH:
        print(f"Password must be at least {PASSWORD_LENGTH} characters long")
        user_password = input("Enter your password: ")
    return user_password


main()

