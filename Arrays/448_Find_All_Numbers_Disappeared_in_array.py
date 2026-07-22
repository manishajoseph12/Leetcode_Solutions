# The Find All Numbers Disappeared in an Array problem is a classic Easy LeetCode question that teaches in-place array manipulation.

# Problem

# You are given an array nums of length n where:

# 1 <= nums[i] <= n
# Some numbers appear twice.
# Others appear once.

# Return all the numbers in the range [1, n] that do not appear in nums.

# -ve method

def findDisappearedNumbers(nums):
    for num in nums:
        index = abs(num) - 1

        if nums[index] > 0:
            nums[index] = -nums[index]

    result = []

    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i + 1)

    return result

# cyclic sorting menthod

# while i < len(nums):
#     correct = nums[i] - 1
#     if nums[i] != nums[correct]:
#         nums[i], nums[correct] = nums[correct], nums[i]
#     else:
#         i += 1

# result = []
# for i in range(len(nums)):
#     if nums[i] != i + 1:
#         result.append(i + 1)