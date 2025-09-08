""" Prime factors of a given number
# 1. Define a class Solution.
# 2. Inside it, create a method prime_factors that takes a number n.
# 3. Initialize an empty list result.
# 4. Loop i from 2 to n:
#    - While n % i == 0:
#        - Append i to result
#        - n //= i
# 5. Return result.
# 6. Take user input for number.
# 7. Create a Solution object.
# 8. Call prime_factors and print result."""

class Solution:
    def prime_factors(self, n: int) -> list:
        result = []
        i = 2
        while i <= n:
            while n % i == 0:
                result.append(i)
                n //= i
            i += 1
        return result

num = int(input("Enter a number: "))
sol = Solution()
result = sol.prime_factors(num)
print("Prime factors:", result)
