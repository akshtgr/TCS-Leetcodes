""" Find all factors of a natural number
# 1. Define a class Solution.
# 2. Inside it, create a method factors that takes a number n.
# 3. Initialize an empty list result.
# 4. Loop i from 1 to n (inclusive):
#    - If n % i == 0, append i to result.
# 5. Return result.
# 6. Take user input for number.
# 7. Create a Solution object.
# 8. Call factors and print result."""

class Solution:
    def factors(self, n: int) -> list:
        result = []
        for i in range(1, n + 1):
            if n % i == 0:
                result.append(i)
        return result

num = int(input("Enter a number: "))
sol = Solution()
result = sol.factors(num)
print("Factors of the number:", result)
