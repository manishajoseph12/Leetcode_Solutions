#second largest number

nums = [4,8,9,6]

first = second = None

for num in nums:
    if first is None or num > first:  
        second = first
        first = num
        #continue

    elif second is None or num > second:
        second = num

print(second)

#4, 