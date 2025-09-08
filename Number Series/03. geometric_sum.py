""" Sum of geometric series
# 1. Define a class Solution.
# 2. Inside it, create a method geometric_sum that takes first term a, common ratio r, and number of terms n.
# 3. Initialize total = 0.
# 4. Initialize current_term = a.
# 5. Loop i from 0 to n-1:
#    - total += current_term
#    - current_term *= r
# 6. Return total.
# 7. Take user input for a, r, n.
# 8. Create a Solution object.
# 9. Call geometric_sum and print result."""

class Solution:
    def geometric_sum(self, a: int, r: int, n: int) -> int:
        total = 0
        current_term = a
        for i in range(n):
            total += current_term
            current_term *= r
        return total

a = int(input("Enter first term of series: "))
r = int(input("Enter common ratio: "))
n = int(input("Enter number of terms: "))
sol = Solution()
result = sol.geometric_sum(a, r, n)
print("Sum of geometric series:", result)
