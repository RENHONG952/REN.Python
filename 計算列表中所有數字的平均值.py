def calculate_average(nums):
    if len(nums) == 0:
        return None
    
    return sum(nums) / len(nums)

print(calculate_average([1, 2, 3, 4, 5]))
print(calculate_average([]))
