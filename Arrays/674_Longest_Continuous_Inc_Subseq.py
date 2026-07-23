#LeetCode #674 – Longest Continuous Increasing Subsequence.
# [1, 2, 3, 1, 2, 3, 4, 5]
# Output:
# 5
# The longest continuous increasing subsequence is:
# [1, 2, 3, 4, 5]


def longest_increasing_subarray(nums):
    longest = 1
    current = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current += 1
        else:
            current = 1

        if current > longest:
            longest = current

    return longest

print(longest_increasing_subarray([1,2,3,1,2,3,4,5]))