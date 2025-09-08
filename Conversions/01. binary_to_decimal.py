""" Convert Binary to Decimal
# 1. Define a class Solution.
# 2. Inside it, create a method binary_to_decimal that takes a binary string s.
# 3. Initialize decimal = 0, power = 0.
# 4. Loop through the binary string from right to left:
#    - decimal += int(bit) * (2 ** power)
#    - power += 1
# 5. Return decimal.
# 6. Take user input for binary string.
# 7. Create a Solution object.
# 8. Call binary_to_decimal and print result."""

class Solution:
    def binary_to_decimal(self, s: str) -> int:
        decimal = 0
        power = 0
        for bit in reversed(s):
            decimal += int(bit) * (2 ** power)
            power += 1
        return decimal

binary_str = input("Enter a binary number: ")
sol = Solution()
result = sol.binary_to_decimal(binary_str)
print("Decimal value:", result)
