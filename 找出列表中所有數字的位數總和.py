def total(n):
    result = {}
    calculate = 0

    for i in n:
        str_i = str(i)
        for j in range(len(str_i)):
            calculate += int(str_i[j])
        result.update({i: calculate})
        calculate = 0
    
    return result

print(total([123, 45, 6]))