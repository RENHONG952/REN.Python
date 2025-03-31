def lenth(a):
    result = {}

    for i in a:
        str_i = str(i)
        result.update({i:len(str_i)})

    return result

print(lenth([123, 45, 6]))