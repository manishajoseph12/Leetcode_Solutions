#LeetCode #169 – Majority Element

def maj(nums):
    element=None
    count=0
    for num in nums:
        if count==0:
            element=num
        if element==num:
            count+=1
        else:
            count-=1
    return element
  







nums = [2,2,1,1,1,1,1,2,2]
print(maj(nums))