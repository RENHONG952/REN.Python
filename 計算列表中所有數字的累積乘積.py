def cumulative_product(nums):
    total = 1
    result = []

    for num in nums:
        total *= num
        result.append(total)
    return result

print(cumulative_product([1, 2, 3, 4]))
print(cumulative_product([5, 10, 2]))
print(cumulative_product([]))