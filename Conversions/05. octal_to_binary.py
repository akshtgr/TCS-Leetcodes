""" Convert Octal to Binary
# 1. Define a class Solution.
# 2. Inside it, create a method octal_to_decimal that converts octal to decimal.
# 3. Then convert decimal to binary using previous method.
# 4. Initialize decimal = 0, power = 0.
# 5. Loop through octal string from right to left:
#    - decimal += int(digit) * (8 ** power)
#    - power += 1
# 6. Convert decimal to binary manually.
# 7. Take user input for octal string.
# 8. Create a Solution object.
# 9. Call octal_to_binary and print result."""

class Solution:
    def octal_to_decimal(self, s: str) -> int:
        decimal = 0
        power = 0
        for digit in reversed(s):
            decimal += int(digit) * (8 ** power)
            power += 1
        return decimal

    def octal_to_binary(self, s: str) -> str:
        decimal = self.octal_to_decimal(s)
        if decimal == 0:
            return "0"
        binary = ""
        temp = decimal
        while temp > 0:
            binary = str(temp % 2) + binary
            temp //= 2
        return binary

octal_str = input("Enter an octal number: ")
sol = Solution()
result = sol.octal_to_binary(octal_str)
print("Binary value:", result)
