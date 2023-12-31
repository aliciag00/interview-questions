# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.

def reverse_string(s):
    left, right = 0, len(s) - 1 # left points to the beginning and right points to the end of array
    # it swaps the characters at these points

    while left < right: #keeps going as long as left os less than right
        s[left], s[right] = s[right], s[left] # swaps the characters
        left += 1
        right -= 1 # moves pointers

s1 = ["a", "w", "e", "s", "o", "m", "e"]
reverse_string(s1)
print(s1)

s2 = ["s", "o", "f", "t", "b", "a", "l", "l"]
reverse_string(s2)
print(s2)
