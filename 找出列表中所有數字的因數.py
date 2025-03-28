def find_factors(nums):
    factors = {}
    for i in range(len(nums)):
        for j in range(1, nums[i] + 1):
            if nums[i] % j == 0:
                if nums[i] in factors:
                    factors[nums[i]].append(j)
                else:
                    factors[nums[i]] = [j]

    return factors

print(find_factors([10, 15, 21]))
print(find_factors([7, 28]))