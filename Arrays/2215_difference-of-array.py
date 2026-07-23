# LeetCode 2215: Find the Difference of Two Arrays

# Given two integer arrays nums1 and nums2, return:

# All distinct integers in nums1 that are not in nums2.
# All distinct integers in nums2 that are not in nums1.

# Answer:
# [result1, result2]

# nums1 = [1,2,3]
# nums2 = [2,4,6]

# Output:
# [[1,3],[4,6]]

def findDifference(self, nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    return [list(set1 - set2), list(set2 - set1)]