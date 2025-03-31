def exponent(n):
    result = {}

    for num in n:
        if num % 2 != 0:
            result.update({num: num ** 3})

    return result

print(exponent([1, 2, 3, 4, 5]))