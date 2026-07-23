# #Medium Array Problem: Product of Array Except Self
# input = [2,3,1,0]
# answer = [1, 2, 6, 6]

def product_except_self(nums):
    n = len(nums)
    answer = [1] * n
 
    # Step 1: Left products
    left = 1
    for i in range(n):
        answer[i] = answer[i] * left
        left = left * nums[i]
 
    # Step 2: Right products
    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] = answer[i] * right
        right = right * nums[i]
 
    return answer



print(product_except_self([2,3,1,0]))