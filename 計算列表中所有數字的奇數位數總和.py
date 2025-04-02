def sum_of_odd_digit_numbers(nums):
    if len(nums) == 0:
        return 0

    total = 0

    for a in range(len(nums)):
        str_a = str(nums[a])
        for b in range(len(str_a)):
            if int(str_a[b]) % 2 != 0:
                total += int(str_a[b])
    return total

print(sum_of_odd_digit_numbers([123, 456, 789]))
print(sum_of_odd_digit_numbers([135, 246]))
print(sum_of_odd_digit_numbers([0, 22, 333]))
print(sum_of_odd_digit_numbers([]))