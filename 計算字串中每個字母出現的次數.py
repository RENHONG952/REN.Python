import re
from collections import Counter

def count_characters(s):
    return dict(Counter(re.sub(r'[\W]', '', s.lower())))

print(count_characters('hello world'))