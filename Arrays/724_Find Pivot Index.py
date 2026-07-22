# LeetCode 724 – Find Pivot Index
# Problem:
# Given an array of integers, return the pivot index where:
# Sum of elements to the left = Sum of elements to the right
# If no such index exists, return -1.

def pivotIndex(nums):
    total = sum(nums)
    left = 0

    for i in range(len(nums)):
        right = total - left - nums[i]

        if left == right:
            return i

        left += nums[i]

    return -1