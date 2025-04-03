def calculate_squares(nums):
    calculate_dic = {}

    for a in nums:
        calculate_dic.update({a:a**2})
    
    return calculate_dic

print(calculate_squares([1, 2, 3, 4]))
print(calculate_squares([5, 10, 15]))
print(calculate_squares([]))