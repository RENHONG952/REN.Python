def remove_duplicates(nums):
    appear = []

    for num in nums:
        if num not in appear:
            appear.append(num)
        else:
            continue 
    return appear

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(remove_duplicates([10, 20, 10, 30, 20]))
print(remove_duplicates([]))