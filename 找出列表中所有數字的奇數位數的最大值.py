def max_of_odd_digit_numbers(nums):
     max_value = 0

     if len(nums) == 0:
          return None
     
     for a in nums:
          for b in range(len(str(a))):
               if int(str(a)[b]) % 2 != 0 and int(str(a)[b]) > max_value:
                    max_value = int(str(a)[b])
     
     if max_value == 0:
          return None
     else:
          return max_value
                          
print(max_of_odd_digit_numbers([123, 456, 789]))
print(max_of_odd_digit_numbers([246, 802]))
print(max_of_odd_digit_numbers([135, 246]))
print(max_of_odd_digit_numbers([]))