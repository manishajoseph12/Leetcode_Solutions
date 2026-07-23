#LeetCode #128. Longest Consecutive Sequence
# nums = [1, 2, 3, 4, 10, 11]
# 1, 2, 3, 4
# Output: 4

def longest(nums):
    n=len(nums)
    num=sorted(nums)
    print(num)
    res=[]
    count=1
    longest=1
    for i in range(n-1):
        if num[i+1] == num[i]+1:
            res.append(num[i])
            count+=1
        else:
            count=1
        if count >longest:
            longest=count
    return (longest)
          # min=float('-inf')
    # for i in range(n):
    #     if nums[i] != None or nums[i]<min:
           
    #         res.append(nums[i])
    #     else:
    #         print(nums)
    #         min=nums[i]
    # return res
      







nums = [1,2,3,4,10,11]
print(longest(nums))


