import math

def calculate_square_roots(nums):
    square = {}
    for num in nums:
        square[num] = round(math.sqrt(num),2)
    return square

print(calculate_square_roots([4, 9, 16]))
print(calculate_square_roots([2, 3, 5]))