# 26 Remove Duplicates from Sorted Array
# Given a sorted integer array nums, remove the duplicates in-place such that each unique element appears only once.
# Return the number of unique elements k.
 
# nums = [1,1,2]
# 2


def remove_duplicates(nums):
    if not nums:
        return 0

    k = 1  # Position to place 

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k

print(remove_duplicates([1,1,2]))