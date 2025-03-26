import re

def is_palindrome(s):
    s = re.sub(r'\W', '', s).lower()
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))