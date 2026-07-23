#Largest Consecutive Range
#To find the start and end values of the longest consecutive sequence.

def largest_range(nums):
    nums = sorted(set(nums))

    best_start = nums[0]
    best_end = nums[0]

    current_start = nums[0]

    for i in range(1, len(nums)):

        if nums[i] - nums[i - 1] == 1:

            if nums[i] - current_start > best_end - best_start:
                best_start = current_start
                best_end = nums[i]

        else:
            current_start = nums[i]

    return [best_start, best_end]