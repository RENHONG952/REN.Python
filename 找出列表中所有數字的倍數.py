def find_multiples(nums, n):
    multiples = []
    for num in nums:
        if num % n == 0:
            multiples.append(num)
    return multiples

print(find_multiples([1, 2, 3, 4, 5, 6], 2))
print(find_multiples([10, 15, 20, 25, 30], 5))