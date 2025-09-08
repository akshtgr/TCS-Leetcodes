""" Replace all ‘0’ with ‘5’ in an input Integer
# 1. Define a class Solution.
# 2. Inside it, create a method replace_zero that takes a number n.
# 3. Initialize result = 0, multiplier = 1.
# 4. Loop while n > 0:
#    - digit = n % 10
#    - If digit == 0, digit = 5
#    - result += digit * multiplier
#    - multiplier *= 10
#    - n = n // 10
# 5. Return result.
# 6. Take user input for number.
# 7. Create a Solution object.
# 8. Call replace_zero and print result."""

class Solution:
    def replace_zero(self, n: int) -> int:
        result = 0
        multiplier = 1
        while n > 0:
            digit = n % 10
            if digit == 0:
                digit = 5
            result += digit * multiplier
            multiplier *= 10
            n //= 10
        return result

num = int(input("Enter a number: "))
sol = Solution()
result = sol.replace_zero(num)
print("Number after replacing 0 with 5:", result)
