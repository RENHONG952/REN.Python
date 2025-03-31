def judge_number(s):
    result = {}

    for i in s:
        if i % 2 == 0:
            result.update({i: "even"})
        else:
            result.update({i: "odd"})

    return result

print(judge_number([1, 2, 3, 4, 5]))