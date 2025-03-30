import re

def reverse_words(s):
    if s == "":
        return ""
        
    s = re.sub(r'[^\W\S]', '',s).split()
    s = [word[::-1] for word in s]
    return ' '.join(s)

print(reverse_words("hello world"))
print(reverse_words("Python is fun"))
print(reverse_words(""))