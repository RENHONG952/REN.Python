def fibonacci(a):
    calculate = [0, 1]

    if a == 0:
        return [0]
    elif a == 1:
        return [0, 1]
    else:
        for i in range(2, a + 1):
            calculate.append(calculate[i-1] + calculate[i-2])
        return calculate
    
print(fibonacci(10)) 