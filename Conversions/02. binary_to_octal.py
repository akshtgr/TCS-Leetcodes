""" Convert Binary to Octal
# 1. Define a class Solution.
# 2. Inside it, create a method binary_to_octal that takes a binary string s.
# 3. First convert binary to decimal using previous method.
# 4. Then convert decimal to octal manually.
# 5. Initialize octal = "", temp = decimal
# 6. Loop while temp > 0:
#    - octal = str(temp % 8) + octal
#    - temp //= 8
# 7. Return octal string.
# 8. Take user input for binary string.
# 9. Create a Solution object.
# 10. Call binary_to_octal and print result."""

class Solution:
    def binary_to_decimal(self, s: str) -> int:
        decimal = 0
        power = 0
        for bit in reversed(s):
            decimal += int(bit) * (2 ** power)
            power += 1
        return decimal

    def binary_to_octal(self, s: str) -> str:
        decimal = self.binary_to_decimal(s)
        if decimal == 0:
            return "0"
        octal = ""
        temp = decimal
        while temp > 0:
            octal = str(temp % 8) + octal
            temp //= 8
        return octal

binary_str = input("Enter a binary number: ")
sol = Solution()
result = sol.binary_to_octal(binary_str)
print("Octal value:", result)
