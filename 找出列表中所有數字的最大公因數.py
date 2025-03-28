def find_gcd(nums):
    gcd = {}

    if len(nums) == 0:
        return None
    
    for i in range(1, min(nums) + 1):
        for j in range(len(nums)):
            if nums[j] % i == 0:
                gcd.update({i: 1})
            else:
                gcd.update({i: 0})
                break
    return max([key for key, value in gcd.items() if value == 1])

print(find_gcd([12, 15, 21]))
print(find_gcd([8, 16, 32]))
print(find_gcd([]))