def longest_word(s):
    if s == "":
        return ""
    
    s = s.split()
    length = len(s[0])
    text = s[0]

    for i in range(len(s)):
        if len(s[i]) > length:
            length = len(s[i]) 
            text = s[i]

    return text

print(longest_word("The quick brown fox jumps over the lazy dog"))
print(longest_word("Python is amazing"))
print(longest_word(""))