def calculate_cubes(nums):
    cubes = {}
    for num in nums:
        cubes[num] = num ** 3
    return cubes

print(calculate_cubes([2, 3, 4]))
print(calculate_cubes([1, 5, 10]))