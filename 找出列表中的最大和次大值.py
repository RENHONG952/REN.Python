def find_two_largest(nums):
    max1 = max(nums)
    for i in range(len(nums)):
        if nums[i] == max1:
            nums[i] = 0
    max2 = max(nums)
    return max1, max2

print(find_two_largest([10, 20, 4, 45, 99]))