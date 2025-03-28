import math

def  calculate_factorials(nums):
    factorials = {}
    for num in nums:
        factorials[num] = math.factorial(num)
    return factorials

print(calculate_factorials([3, 4, 5]))
print(calculate_factorials([0, 1, 2]))
