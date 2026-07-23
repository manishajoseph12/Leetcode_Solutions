#LeetCode #387 First Unique Character in a String problem

def first_unique_char(s):
    count = {}

    # Count frequency
    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    # Find first unique character
    # for ch in s:
    #     if count[ch] == 1:
    #         return ch
    for k,v in count.items():
        if v==1:
            return (k)
            break


s = "aagbbccdde"
print(first_unique_char(s))