def min_of_odd_digit_numbers(nums):
    min_value = 1
    detection = False    

    if len(nums) == 0:
        return None
    
    for a in nums:
        for b in range(len(str(a))):
            if int(str(a)[b]) % 2 != 0 and int(str(a)[b]) <= min_value:
                min_value = int(str(a)[b])
                detection = True

    if detection == True:
        return min_value
    else:
        return None
        
print(min_of_odd_digit_numbers([123, 456, 789]))
print(min_of_odd_digit_numbers([246, 802]))
print(min_of_odd_digit_numbers([135, 246]))
print(min_of_odd_digit_numbers([]))