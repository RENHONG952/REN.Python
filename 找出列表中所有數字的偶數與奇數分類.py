def classify_even_odd(nums):
    even = []
    odd = []

    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return {'even': even, 'odd': odd}

print(classify_even_odd([1, 2, 3, 4, 5, 6]))
print(classify_even_odd([10, 15, 20, 25]))