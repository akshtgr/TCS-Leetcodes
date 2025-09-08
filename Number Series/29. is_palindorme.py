""" Check if a number is Palindrome
# 1. Define a class Solution.
# 2. Inside it, create a method is_palindrome that takes a number n.
# 3. Store original number in temp.
# 4. Initialize rev = 0.
# 5. Loop while n > 0:
#    - rev = rev * 10 + n % 10
#    - n //= 10
# 6. If rev == temp, return True, else False.
# 7. Take user input for number.
# 8. Create a Solution object.
# 9. Call is_palindrome and print result."""

class Solution:
    def is_palindrome(self, n: int) -> bool:
        temp = n
        rev = 0
        while n > 0:
            rev = rev * 10 + n % 10
            n //= 10
        return rev == temp

num = int(input("Enter a number: "))
sol = Solution()
result = sol.is_palindrome(num)
print(f"Is {num} a Palindrome?:", result)
