""" Can a number be expressed as a sum of two prime numbers
# 1. Define a class Solution.
# 2. Inside it, create a method is_prime for checking primality.
# 3. Create a method sum_of_two_primes that takes n.
# 4. Loop i from 2 to n//2:
#    - If i and n-i are prime, return True
# 5. If no such pair found, return False.
# 6. Take user input for n.
# 7. Create a Solution object.
# 8. Call sum_of_two_primes and print result."""

class Solution:
    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def sum_of_two_primes(self, n: int) -> bool:
        for i in range(2, n//2 + 1):
            if self.is_prime(i) and self.is_prime(n - i):
                return True
        return False

n = int(input("Enter a number: "))
sol = Solution()
result = sol.sum_of_two_primes(n)
print(f"Can {n} be expressed as sum of two prime numbers?:", result)
