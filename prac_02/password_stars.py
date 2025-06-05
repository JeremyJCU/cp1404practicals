"""Valid password check and length display using star character"""
PASSWORD_LENGTH = 10
user_password = input("Enter your password: ")
while len(user_password) < PASSWORD_LENGTH:
    print(f"Password must be at least {PASSWORD_LENGTH} characters long")
    user_password = input("Enter your password: ")
print("*" * len(user_password))

