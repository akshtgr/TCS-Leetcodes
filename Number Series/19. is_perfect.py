""" Perfect Number
# 1. Define a class Solution.
# 2. Inside it, create a method is_perfect that takes a number n.
# 3. Initialize sum_div = 0.
# 4. Loop i from 1 to n-1:
#    - If n % i == 0, sum_div += i
# 5. If sum_div == n, return True, else False.
# 6. Take user input for number.
# 7. Create a Solution object.
# 8. Call is_perfect and print result."""

class Solution:
    def is_perfect(self, n: int) -> bool:
        sum_div = 0
        for i in range(1, n):
            if n % i == 0:
                sum_div += i
        return sum_div == n

num = int(input("Enter a number: "))
sol = Solution()
result = sol.is_perfect(num)
print(f"Is {num} a Perfect Number?:", result)
