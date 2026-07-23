# LeetCode problem: #53 – Maximum Subarray.

# Problem: Given an integer array nums, find the contiguous subarray with the largest sum and return that sum.

# Example:
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Output:
# 6

#Method:1

def max_subarray(nums):
    curr_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):

        if curr_sum < 0:
            curr_sum = nums[i]
        else:
            curr_sum = curr_sum + nums[i]

        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum


#Method:2
def max_subarray(nums):

    curr_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):

        curr_sum = max(nums[i], curr_sum + nums[i])

        max_sum = max(max_sum, curr_sum)

    return max_sum




#Method:3
def max_subarray(nums):
    curr_sum = 0
    max_sum = float("-inf")

    for num in nums:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)

    return max_sum

#Method:3 without Max


