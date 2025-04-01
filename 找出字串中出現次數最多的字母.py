import re
from collections import Counter

def most_frequent_letter(s):
    if len(s) == 0:
        return None
    
    sort = []
    s = re.sub(r"[^a-zA-Z]","",s).lower()
    counter = Counter(s)
    most_common_frequency = counter.most_common(1)[0][1]
    
    for char, freq in counter.items():
        if freq == most_common_frequency:
            sort.append(char)
    
    return ''.join(sorted(sort[0]))

print(most_frequent_letter("Hello World!"))
print(most_frequent_letter("Python Programming"))
print(most_frequent_letter(""))