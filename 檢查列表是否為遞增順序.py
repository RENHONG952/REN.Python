def is_sorted(nums):
    calculate = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < calculate:
            return False
        calculate = nums[i]
    return True

print(is_sorted([1, 2, 3, 4, 5]))