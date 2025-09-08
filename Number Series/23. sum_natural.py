""" Sum of first n natural numbers
# 1. Define a class Solution.
# 2. Inside it, create a method sum_natural that takes n.
# 3. Initialize total = 0.
# 4. Loop i from 1 to n:
#    - total += i
# 5. Return total.
# 6. Take user input for n.
# 7. Create a Solution object.
# 8. Call sum_natural and print result."""

class Solution:
    def sum_natural(self, n: int) -> int:
        total = 0
        for i in range(1, n + 1):
            total += i
        return total

n = int(input("Enter n: "))
sol = Solution()
result = sol.sum_natural(n)
print("Sum of first n natural numbers:", result)
