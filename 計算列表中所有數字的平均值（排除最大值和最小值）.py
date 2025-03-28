def average_excluding_extremes(nums):
    if len(nums) <= 2:
        return None

    nums = sorted(nums)[1:-1]
    return sum(nums) / len(nums)

print(average_excluding_extremes([1, 2, 3, 4, 5]))
print(average_excluding_extremes([10, 10, 10]))
print(average_excluding_extremes([1, 2]))
print(average_excluding_extremes([]))