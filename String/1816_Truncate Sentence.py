#1816. Truncate Sentence
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
# Each of the words consists of only uppercase and lowercase English letters (no punctuation).
# For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
# You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. 
# Return s​​​​​​ after truncating it.

def truncateSentence(s: str, k: int) -> str:
    space_count = 0
    
    for i in range(len(s)):
        if s[i] == ' ':
            space_count += 1
            if space_count == k:
                return s[:i]
    
    return s
s = "Hello how are you Contestant"
k = 4
print(truncateSentence(s,k))



# s = "Hello How Are You Contestant"
# k=4
# words = s.split()

#         # 2. Slice the list to keep only the first 'k' words
# truncated_words = words[:k]

#         # 3. Join them back together with a space
# print(" ".join(truncated_words))