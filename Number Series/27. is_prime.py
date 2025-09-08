""" Count prime numbers that can be expressed as sum of consecutive prime numbers
# 1. Define a class Solution.
# 2. Inside it, create a method is_prime for checking primality.
# 3. Create a method count_prime_sums that takes limit n.
# 4. Generate all primes <= n.
# 5. Loop start index from 0 to len(primes)-1:
#    - Loop end index from start to len(primes)-1:
#        - sum consecutive primes
#        - If sum <= n and sum is prime, add to set
# 6. Return length of set.
# 7. Take user input for n.
# 8. Create a Solution object.
# 9. Call count_prime_sums and print result."""

class Solution:
    def is_prime(self, num: int) -> bool:
        if num <= 1:
            return False
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True

    def count_prime_sums(self, n: int) -> int:
        primes = []
        for i in range(2, n + 1):
            if self.is_prime(i):
                primes.append(i)
        sums_set = set()
        for start in range(len(primes)):
            total = 0
            for end in range(start, len(primes)):
                total += primes[end]
                if total <= n and self.is_prime(total):
                    sums_set.add(total)
        return len(sums_set)

n = int(input("Enter a number: "))
sol = Solution()
result = sol.count_prime_sums(n)
print("Count of prime numbers expressible as sum of consecutive primes:", result)
