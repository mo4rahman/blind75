# https://leetcode.com/problems/contains-duplicate/
# Easy
# Problem 217
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


# O(n) time: worst case, in the case it is false, run through entire array once with for loop
# O(n) Space Complexity
# better than using set
def contains_duplicate(nums):
    """Return true if any value appears at least twice in the array. Return false if every element is distinct."""
    # hash_map = {}
    # for number in nums:
    #     if number in hash_map:
    #         return True
    #     hash_map[number] = 1
    hash_set = set()  # {}
    for number in nums:
        if number in hash_set:
            return True
        hash_set.add(number)
    return False

#O(nlogn) time
# O(1) space
# Method 2 -- Sorting
# l =  len(nums)
# if l < 2:
#     return False
# nums.sort()
# for i in range(l-1):
#     if nums[i] == nums[i+1]:
#         return True
# return False

# set needs to convert entire array into set first 
def contains_duplicate2(nums):
    # nums_set = list(set(nums))
    # if (nums_set) == nums:
    #     return False
    # return True
    # return list(set(nums)) != nums
    return len(set(nums)) != len(nums)

print(contains_duplicate2([1, 2, 3, 4, 4]))
