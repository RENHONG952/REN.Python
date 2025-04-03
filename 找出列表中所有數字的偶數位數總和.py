def sum_of_even_digit_numbers(nums):
    total = 0
    
    if len(nums) == 0:
        return 0
    
    for a in nums:
        for b in range(len(str(a))):
            if int(str(a)[b]) % 2 == 0:
                total += int(str(a)[b])
    
    return total

print(sum_of_even_digit_numbers([123, 456, 789]))
print(sum_of_even_digit_numbers([135, 246]))
print(sum_of_even_digit_numbers([0, 22, 333]))
print(sum_of_even_digit_numbers([]))