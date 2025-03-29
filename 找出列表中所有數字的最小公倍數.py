import math

def find_lcm(nums):
    if len(nums) == 0:
        return None
    
    return math.lcm(*nums)

print(find_lcm([4, 6, 8]))
print(find_lcm([3, 7, 21]))
print(find_lcm([]))