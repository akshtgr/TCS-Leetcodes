""" Square Free Number
# 1. Define a class Solution.
# 2. Inside it, create a method is_square_free that takes a number n.
# 3. Loop i from 2 to sqrt(n):
#    - If n % (i*i) == 0, return False
# 4. If no i found, return True.
# 5. Take user input for number.
# 6. Create a Solution object.
# 7. Call is_square_free and print result."""

class Solution:
    def is_square_free(self, n: int) -> bool:
        i = 2
        while i * i <= n:
            if n % (i * i) == 0:
                return False
            i += 1
        return True

num = int(input("Enter a number: "))
sol = Solution()
result = sol.is_square_free(num)
print(f"Is {num} a Square Free Number?:", result)
