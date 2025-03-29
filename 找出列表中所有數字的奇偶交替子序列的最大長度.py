def max_alternating_subsequence(nums):
    if not nums:
        return 0
    
    length = 1
    for i in range(1, len(nums)):
        if nums[i] % 2 != nums[i - 1] % 2:
            length += 1
        
    return length

print(max_alternating_subsequence([1, 2, 3, 4, 5]))
print(max_alternating_subsequence([1, 3, 5, 7]))
print(max_alternating_subsequence([2, 4, 6, 8]))
print(max_alternating_subsequence([1, 2, 2, 3, 4]))
print(max_alternating_subsequence([]))