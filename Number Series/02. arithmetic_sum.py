""" Sum of arithmetic series
# 1. Define a class Solution.
# 2. Inside it, create a method arithmetic_sum that takes first term a, common difference d, and number of terms n.
# 3. Initialize total = 0.
# 4. Loop i from 0 to n-1:
#    - total += a + i*d
# 5. Return total.
# 6. Take user input for a, d, n.
# 7. Create a Solution object.
# 8. Call arithmetic_sum and print result."""

class Solution:
    def arithmetic_sum(self, a: int, d: int, n: int) -> int:
        total = 0
        for i in range(n):
            total += a + i*d
        return total

a = int(input("Enter first term of series: "))
d = int(input("Enter common difference: "))
n = int(input("Enter number of terms: "))
sol = Solution()
result = sol.arithmetic_sum(a, d, n)
print("Sum of arithmetic series:", result)
