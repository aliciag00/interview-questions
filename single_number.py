# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.


# This searches an array to see if any number is not listed twice
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Given an array, python will print the single number using function above
nums = [2, 2, 3, 3, 5, 4, 5,]
print(single_number(nums))

nums = [ 1, 2, 3, 2, 3,]
print(single_number(nums))
