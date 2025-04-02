def find_prime_factors(nums):
    if len(nums) == 0:
        return {}

    calculate_dic = {}

    for a in range(len(nums)):
        calculate = []
        new_calculate = []
        for b in range(2,nums[a] + 1):
            if nums[a] % b == 0:
                calculate.append(b)
        loop = 0
        calculate_original = nums[a]
        while calculate_original != 1:
            if calculate_original % calculate[loop] == 0:
                new_calculate.append(calculate[loop])
                calculate_original = calculate_original / calculate[loop]
            else:
                loop += 1
        calculate_dic.update({nums[a]:new_calculate})
    return calculate_dic

print(find_prime_factors([12, 15, 7]))  
print(find_prime_factors([28, 45]))     
print(find_prime_factors([]))           