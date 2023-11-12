# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

# Example 1:

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.
# Example 2:

# Input: num = 0
# Output: 0
 

# Constraints:

# 0 <= num <= 231 - 1

def add_digits(num):
    while num >= 10: # while loop keeps looking to sum the digits until theres only a single digit
        num = sum(int(digit) for digit in str(num)) # calculates the some of the digits by converting the number to a string, back, then adding
    return num

print(add_digits(56))
print(add_digits(989))
print(add_digits(8))