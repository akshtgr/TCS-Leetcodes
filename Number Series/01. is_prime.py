""" Prime Numbers
# 1. Define a class Solution.
# 2. Inside it, create a method is_prime that takes a number n.
# 3. If n <= 1, return False (not prime).
# 4. Loop from 2 to sqrt(n) (inclusive) and check if n is divisible by any number.
# 5. If divisible, return False.
# 6. Otherwise, return True.
# 7. Take user input for a number.
# 8. Create a Solution object.
# 9. Call is_prime and print result."""

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

num = int(input("Enter a number to check prime: "))
sol = Solution()
result = sol.is_prime(num)
print(f"Is {num} prime?:", result)
