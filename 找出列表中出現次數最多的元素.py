def most_frequent_element(nums):
    if not nums:
        return None
    
    appear = {}

    for num in nums:
        if num in appear:
            appear[num] += 1
        else:
            appear[num] = 1
    return max(appear, key=appear.get)

print(most_frequent_element([1, 3, 2, 3, 4, 1, 3]))
print(most_frequent_element([5, 5, 6, 6, 7]))
print(most_frequent_element([]))