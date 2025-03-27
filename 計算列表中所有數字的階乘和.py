import math

def sum_of_factorials(nums):
    if len(nums) == 0:
        return 0
    total = 0        
    for num in nums:
        total += math.factorial(num)

    return total

print(sum_of_factorials([1, 2, 3, 4]))
print(sum_of_factorials([5, 6]))
print(sum_of_factorials([]))