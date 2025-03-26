import re
from collections import Counter

def word_count(s):
    s = re.sub(r'[^\w\s]', ' ', s.lower())
    words = s.split()
    return dict(Counter(words))

print(word_count('This is a test. This test is only a test.'))