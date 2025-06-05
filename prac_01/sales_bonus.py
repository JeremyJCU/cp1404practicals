"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
SALES_THRESHOLD = 1000
STANDARD_BONUS = .1
EXTRA_BONUS = .15
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < SALES_THRESHOLD:
        sales_bonus = sales * STANDARD_BONUS
    else:
        sales_bonus = sales * EXTRA_BONUS
    print(f": {sales_bonus}")
    sales = float(input("Enter sales: $"))

