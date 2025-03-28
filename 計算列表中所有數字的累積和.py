def cumulative_sum(nums):
    total = 0
    result = []
    for num in nums:
        total += num
        result.append(total)
    return result

print(cumulative_sum([1, 2, 3, 4]))
print(cumulative_sum([10, 20, 30]))