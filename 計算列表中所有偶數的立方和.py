def sum_of_cubes_of_evens(nums):
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            nums[i] = 0
    
    return sum([a ** 3 for a in nums])

print(sum_of_cubes_of_evens([1, 2, 3, 4, 5, 6]))
print(sum_of_cubes_of_evens([7, 9, 11]))
print(sum_of_cubes_of_evens([]))