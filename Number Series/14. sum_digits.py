""" Sum of digits of a number
# 1. Define a class Solution.
# 2. Inside it, create a method sum_digits that takes a number n.
# 3. Initialize total = 0.
# 4. Loop while n > 0:
#    - total += n % 10
#    - n //= 10
# 5. Return total.
# 6. Take user input for number.
# 7. Create a Solution object.
# 8. Call sum_digits and print result."""

class Solution:
    def sum_digits(self, n: int) -> int:
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total

num = int(input("Enter a number: "))
sol = Solution()
result = sol.sum_digits(num)
print("Sum of digits:", result)