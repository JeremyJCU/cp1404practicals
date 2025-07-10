"""CP1404/CP5632 Practical
guitar Time Estimate:
Estimate: 120 minutes
Actual:  150 minutes
"""
from datetime import date
from prac_06.guitar import Guitar

AGE = 50

def main():
    """Test that Guitar class functions work."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    fener = Guitar("Stratoscaster", 2014, 765.30)
    line = Guitar("Line 6 JTV-59", 2010, 1512.90)
    # print(gibson)
    # print(gibson.get_age())
    # print(gibson.is_vintage())

    print("testing class age functions")
    expected_output = date.today().year - gibson.year
    test_guitar(expected_output, gibson, 'age')

    expected_output = date.today().year - fener.year
    test_guitar(expected_output, fener, 'age')

    expected_output = date.today().year - line.year
    test_guitar(expected_output, line, 'age')

    print()
    print("testing class age functions")
    expected_output = gibson.get_age() >= AGE
    test_guitar(expected_output, gibson, 'vintage')

    expected_output = fener.get_age() >= AGE
    test_guitar(expected_output, fener, 'vintage')

    expected_output = line.get_age() >= AGE
    test_guitar(expected_output, line, 'vintage')

def test_guitar(expected_output, guitar, test_type):
    """Generic test function used for all tests"""
    if test_type == 'age':
        print(f"Expected {expected_output}. got {guitar.get_age()}")
    elif test_type == 'vintage':
        print(f"Expected {expected_output}. got {guitar.is_vintage()}")

main()

