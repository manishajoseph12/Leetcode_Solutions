#LeetCode #189 – Rotate Array

def rotate(arr, k):
    n = len(arr)
    k = k % n
    print(k)

    # step 1: reverse whole array
    arr.reverse()
    print(arr)

    # step 2: reverse first k
    left = 0
    right = k - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    # step 3: reverse remaining
    left = k
    right = n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr
arr = [1,2,3,4,5,6,7]
k=7
print(rotate(arr,k))


#2) 
def rotate(arr, k):
    n = len(arr)
    k = k % n
    res = [0] * n

    for i in range(n):
        res[(i + k) % n] = arr[i]

    return res
arr = [1,2,3,4,5,6,7]
k=3
print(rotate(arr,k))
