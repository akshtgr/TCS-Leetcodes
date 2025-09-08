""" Given number is even or odd
# 1. Define a class Solution.
# 2. Inside it, create a method even_or_odd that takes a number n.
# 3. If n % 2 == 0, return "Even", else return "Odd".
# 4. Take user input for number.
# 5. Create a Solution object.
# 6. Call even_or_odd and print result."""

class Solution:
    def even_or_odd(self, n: int) -> str:
        if n % 2 == 0:
            return "Even"
        else:
            return "Odd"

num = int(input("Enter a number: "))
sol = Solution()
result = sol.even_or_odd(num)
print("Number is:", result)
