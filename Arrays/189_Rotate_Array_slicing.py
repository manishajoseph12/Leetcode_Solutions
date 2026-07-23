# LeetCode 189: Rotate Array.

# Problem: Rotate an array to the right by k steps.
# Example:
# nums = [1,2,3,4,5,6,7]
# k = 3

# output:
# [5,6,7,1,2,3,4]

nums = [1,2,3,4,5,6,7]
k = 3
k = k % len(nums)
print(nums[-k:])
print(nums[:-k])
nums = nums[-k:] + nums[:-k]

print(nums)