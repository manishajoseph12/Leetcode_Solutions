# LeetCode 414: Third Maximum Number is about finding the 3rd distinct maximum value in an array.
# We care about distinct values only
# Track top 3 unique maximum numbers while scanning once
# If fewer than 3 distinct numbers exist → return the maximum

def thirdMax(nums):
    first = second = third = None

    for num in nums:
        # skip duplicates
        if num == first or num == second or num == third:
            continue

        if first is None or num > first:
            third = second
            second = first
            first = num

        elif second is None or num > second:
            third = second
            second = num

        elif third is None or num > third:
            third = num

    return third if third is not None else first