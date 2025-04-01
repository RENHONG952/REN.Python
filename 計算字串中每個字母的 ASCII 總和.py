import re

def ascii_sum(s):
    total = 0
    s = re.sub(r"[^a-zA-Z]","",s)
    
    for char in s:
        total += ord(char)
    return total

print(ascii_sum("Hello World!"))
print(ascii_sum("Python 3.9"))
print(ascii_sum(""))