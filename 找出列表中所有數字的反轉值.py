def reverse(n):
    resulte = {}

    for num in n:
        resulte.update({num: int(str(num)[::-1])})
    
    return resulte

print(reverse([123, 45, 6]))