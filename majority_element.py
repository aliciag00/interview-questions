# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 
def majority_element(nums):
    candidate = None # candidate represents the potential majority
    count = 0 # keeps track of balance between the candidate and other elements

    for num in nums: # runs through the array
        if count == 0:
            candidate = num
            count += 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
# if element is present it adds 1 to the count each time it appears

    return candidate

print(majority_element([3, 3, 3, 4, 2, 4]))
print(majority_element([2, 1, 9, 0, 0]))

# uses a linear runtime complexity