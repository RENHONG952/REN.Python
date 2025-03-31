def multiple(x,y):
    result = {}

    for num in x:
        if num % y == 0:
            result.update({num:True})
        else:
            result.update({num:False})

    return result

print(multiple([10, 15, 20, 25], 5))