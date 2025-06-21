"""
CP1404/CP5632 Practical
Program that allows look up hexadecimal colour codes
"""

COLOUR_TO_CODE = {'alicablue': '#f0f8ff', 'absolutezero': '#0048ba', 'babyblue': '#89cff0', 'byzantium': '#702963',
                  'cadetgrey': '#91a3b0', 'cyclamen': '#f56fa1', 'daffodil': '#ffff31', 'dutchwhite': '#efdfbb',
                  'earthyellow': '#e1a95f', 'etonblue': '#96c8a2'}


def main():
    """Program that allows look up hexadecimal colour codes"""
    print(COLOUR_TO_CODE)

    colour_code = input("Enter colour name: ").lower()
    while colour_code != "":
        try:
            print(colour_code, "is", COLOUR_TO_CODE[colour_code])
        except KeyError:
            print("Invalid state")
        colour_code = input("Enter colour name: ").lower()


main()
