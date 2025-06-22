"""
CP1404/CP5632 Practical
A program to count the occurrences of words in a string
Word Occurrences Time Estimate:
Estimate: 30 minutes
Actual: 160 minutes
"""


def main():
    name_to_email = {}
    email = input("Email: ")
    if email != '':
        name_to_email = extraction_of_name(email, name_to_email)
    while email != '' and is_email(email):
        email = input("Email: ")
        if email != '':
            name_to_email = extraction_of_name(email, name_to_email)
    display_name_email(name_to_email)


def extraction_of_name(email, name_to_email):
    name = determine_name(email)
    full_name = create_name(name)
    name = check_name(full_name)
    name_to_email = create_name_map(name, email, name_to_email)
    return name_to_email


def is_email(email):
    """Check if email is an email address"""
    try:
        email.index('@')
        return True
    except ValueError:
        return False


def determine_name(email):
    """Extract potential name from email"""
    slice_end = email.index('@')
    full_name_pre_strip = email[:slice_end]
    full_name = full_name_pre_strip.split('.')
    return full_name


def check_name(name):
    """Check if name from email is a valid name"""
    if input(f"Is your name {name}? (Y/n)").lower() == 'y':
        return name
    else:
        replacement_name = input("Name:")
        name = replacement_name.split()
        name = create_name(name)
        return name


def create_name(name):
    """Create string name from email"""
    if len(name) > 1:
        full_name = "".join(name[0] + " " + name[1]).title()
    else:
        full_name = name[0].title()
    return full_name


def create_name_map(name, email, name_to_email):
    """Add name and email to dictionary"""
    name_to_email[name] = email
    return name_to_email


def display_name_email(name_to_email):
    """Display name and email"""
    for name, email in name_to_email.items():
        print(f"{name} ({email})")


main()
