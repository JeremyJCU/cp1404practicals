# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
#smallest: 8
#largeset:20

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
#smallest: 3
#largest:  7
#Could line 2 have produced a 4?
#No. The first argument was 3. This meant that the start value was too large
#for 4 to ever be chooses with the step value of 2.

# What did you see on line 3?
# 4.845581280493075
#This was expected though as Get a random number in the range [a, b)

# What was the smallest number you could have seen, what was the largest?
#smalleset 2.5
#largest 5.5

""""Write code, not a comment, to produce a random number between 1 and 100 inclusive."""
from random import randint
print(randint(1, 100))