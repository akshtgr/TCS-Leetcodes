""" Reverse digits of a number
# 1. Define a class Solution.
# 2. Inside it, create a method reverse_number that takes number n.
# 3. Initialize rev = 0.
# 4. Loop while n > 0:
#    - rev = rev * 10 + (n % 10)
#    - n //= 10
# 5. Return rev.
# 6. Take user input for number.
# 7. Create a Solution object.
# 8. Call reverse_number and print result."""

class Solution:
    def reverse_number(self, n: int) -> int:
        rev = 0
        while n > 0:
            rev = rev * 10 + (n % 10)
            n //= 10
        return rev

num = int(input("Enter a number: "))
sol = Solution()
result = sol.reverse_number(num)
print("Reversed number:", result)
