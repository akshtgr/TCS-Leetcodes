""" Kth largest factor of number N
# 1. Define a class Solution.
# 2. Inside it, create a method kth_largest_factor that takes n and k.
# 3. Initialize an empty list factors.
# 4. Loop i from 1 to n:
#    - If n % i == 0, append i to factors.
# 5. Sort factors manually in ascending order.
# 6. Return factors[-k] if k <= len(factors), else -1.
# 7. Take user input for n and k.
# 8. Create a Solution object.
# 9. Call kth_largest_factor and print result."""

class Solution:
    def kth_largest_factor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        # Manual sort (ascending)
        for i in range(len(factors)):
            for j in range(0, len(factors)-i-1):
                if factors[j] > factors[j+1]:
                    factors[j], factors[j+1] = factors[j+1], factors[j]
        if k <= len(factors):
            return factors[-k]
        else:
            return -1

n = int(input("Enter a number: "))
k = int(input("Enter k: "))
sol = Solution()
result = sol.kth_largest_factor(n, k)
print(f"{k}th largest factor:", result)
