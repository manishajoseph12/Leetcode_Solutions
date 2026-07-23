def sortedsquares(nums):
    n=len(nums)
    res=[0]*n
    #print(res)
    left,right=0,n-1
    pos=n-1
    while left<=right:
        if nums[left]**2 >nums[right]**2:
            res[pos]=nums[left]**2
            print(res)
            left+=1
        else:
            res[pos]=nums[right]**2
            print(res)
            right-=1
        pos-=1
    return res
print(sortedsquares(nums=[-4,-1,0,3,10]))

