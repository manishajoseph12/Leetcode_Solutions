def countSegments(s: str) -> int:
    count = 0
    
    for i in range(len(s)):
        if s[i] != ' ':
            # 🎉 new word start
            if i == 0:
                count += 1
            elif s[i-1] == ' ':
                count += 1
    
    return count
s= "Hello, my name is John"
print(countSegments(s))