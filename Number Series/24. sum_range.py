""" Sum of all natural numbers in range L to R
# 1. Define a class Solution.
# 2. Inside it, create a method sum_range that takes L and R.
# 3. Initialize total = 0.
# 4. Loop i from L to R:
#    - total += i
# 5. Return total.
# 6. Take user input for L and R.
# 7. Create a Solution object.
# 8. Call sum_range and print result."""

class Solution:
    def sum_range(self, L: int, R: int) -> int:
        total = 0
        for i in range(L, R + 1):
            total += i
        return total

L = int(input("Enter start of range: "))
R = int(input("Enter end of range: "))
sol = Solution()
result = sol.sum_range(L, R)
print("Sum of numbers in range:", result)
