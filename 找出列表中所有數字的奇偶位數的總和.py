def sum_of_even_and_odd_digits(nums):
    odd = 0
    even = 0
    
    for a in nums:
        for b in range(len(str(a))):
            if int(str(a)[b]) % 2 == 0:
                even += int(str(a)[b])
            else:
                odd += int(str(a)[b])
    
    return { 'even': even,'odd': odd}

print(sum_of_even_and_odd_digits([123, 456, 789]))
print(sum_of_even_and_odd_digits([246, 802]))
print(sum_of_even_and_odd_digits([135, 246]))
print(sum_of_even_and_odd_digits([]))