def count_vowels(s):
    monthers = 'aeiou'
    count = 0
    s = s.lower()
    for char in s:
        if char in monthers:
            count += 1
    return count

print(count_vowels("hello world"))
print(count_vowels("Python is amazing"))
print(count_vowels(""))