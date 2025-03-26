def sum_of_squares_of_odds(nums):
    Sum = 0

    if not nums:
        return 0
    
    for a in nums:
        if a % 2 != 0:
            Sum += a ** 2
    return Sum

print(sum_of_squares_of_odds([1, 2, 3, 4, 5]))        