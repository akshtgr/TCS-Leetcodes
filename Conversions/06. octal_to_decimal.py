""" Convert Octal to Decimal
# 1. Define a class Solution.
# 2. Inside it, create a method octal_to_decimal that takes octal string s.
# 3. Initialize decimal = 0, power = 0.
# 4. Loop through s from right to left:
#    - decimal += int(digit) * (8 ** power)
#    - power += 1
# 5. Return decimal.
# 6. Take user input for octal string.
# 7. Create a Solution object.
# 8. Call octal_to_decimal and print result."""

class Solution:
    def octal_to_decimal(self, s: str) -> int:
        decimal = 0
        power = 0
        for digit in reversed(s):
            decimal += int(digit) * (8 ** power)
            power += 1
        return decimal

octal_str = input("Enter an octal number: ")
sol = Solution()
result = sol.octal_to_decimal(octal_str)
print("Decimal value:", result)
