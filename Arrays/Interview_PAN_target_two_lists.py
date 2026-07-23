
#  If you need to return the indices of the numbers (one index from nums1 and one from nums2)
#  whose values add up to the target


# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# target = 8


def two_sum_two_lists(nums1, nums2, target):
    lookup = {}

    for i, num in enumerate(nums1):
        lookup[num] = i


        #lookup= {1:0, 2:1, 3:2}

    for j, num in enumerate(nums2):
        complement = target - num

        #lookup= {8-4}

        if complement in lookup:
            return [lookup[complement], j]

    return None


nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
target = 8
print(two_sum_two_lists(nums1, nums2, target))