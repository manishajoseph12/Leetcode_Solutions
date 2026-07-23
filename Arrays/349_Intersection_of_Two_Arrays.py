#349 — Intersection of Two Arrays
# To return the unique elements common to both arrays.

# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# result = []
# set1 = set(nums1)
# set2 = set(nums2)
# for num in set2:
#     if num in set1:
#         result.append(num)

# print(result)


def intersection(nums1, nums2):
    set1 = set(nums1)   # store elements from nums1
    result = []         # store answer

    for num in nums2:
        if num in set1:
            if num not in result:   # avoid duplicates
                result.append(num)

    return result


# Test
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersection(nums1, nums2))