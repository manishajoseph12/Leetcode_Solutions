# LeetCode 217: Contains Duplicate is one of the easiest and most common hash set/hash map interview problems.
# Problem
# Given an integer array nums, return:
# True if any value appears at least twice.
# False if every element is unique.
# Example 1
# Input: nums = [1,2,3,1]
# Output: True

def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

print(containsDuplicate([1,2,3,1]))