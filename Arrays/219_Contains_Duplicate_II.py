#LeetCode 219 — Contains Duplicate II
# nums = [1, 2, 3, 1]
#k = 3
# The duplicate 1s are at indices 0 and 3:
#abs(3 - 0) = 3 <= k
# Answer: True

nums = [1,2,3,1]
k = 3

dup = {}

def contains_dup_two(nums,k):
    for i , num in enumerate(nums):
        if num not in dup:
            dup[num] = i

        else:
            if i - dup[num] <= k:
                return True
        

    return False

print(contains_dup_two([1,2,3,1],3))