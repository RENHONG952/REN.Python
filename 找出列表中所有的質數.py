def find_primes(nums):
    primes = []
    for num in nums:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

print(find_primes([2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))