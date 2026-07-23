def sortedSquares(nums):
    n = len(nums)
    res = [0] * n

    # Step 1: find split point
    right = 0
    while right < n and nums[right] < 0:
        right += 1
    left = right - 1

    pos = 0

    # Step 2: merge
    while left >= 0 and right < n:
        if nums[left]**2 < nums[right]**2:
            res[pos] = nums[left]**2
            left -= 1
        else:
            res[pos] = nums[right]**2
            right += 1
        pos += 1

    # Step 3: remaining elements
    while left >= 0:
        res[pos] = nums[left]**2
        left -= 1
        pos += 1

    while right < n:
        res[pos] = nums[right]**2
        right += 1
        pos += 1

    return res


print(sortedSquares([-4, -1, 0, 3, 10]))
