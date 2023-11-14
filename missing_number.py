# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

# Constraints:

# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.

def missing_number(nums):
    n = len(nums) # calculating the length of the list of numbers
    expected_sum = n * (n + 1) // 2 # calculating the sum of the first natural numbers 
    actual_sum = sum(nums)
# the missing number will be the difference between the sum of the natural numbers and the sum of the array
    return expected_sum - actual_sum
# returns missing number
nums1 = [0, 1, 3, 4]
print(missing_number(nums1))

nums2 = [0, 1, 2, 3, 4, 6, 7, 8, 9]
print(missing_number(nums2))

nums3 = [0, 1, 2]
print(missing_number(nums3))