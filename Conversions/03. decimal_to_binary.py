""" Decimal to Binary conversion
# 1. Define a class Solution.
# 2. Inside it, create a method decimal_to_binary that takes a decimal number n.
# 3. Initialize binary = "", temp = n
# 4. Loop while temp > 0:
#    - binary = str(temp % 2) + binary
#    - temp //= 2
# 5. Handle case n = 0 separately.
# 6. Return binary string.
# 7. Take user input for decimal number.
# 8. Create a Solution object.
# 9. Call decimal_to_binary and print result."""

class Solution:
    def decimal_to_binary(self, n: int) -> str:
        if n == 0:
            return "0"
        binary = ""
        temp = n
        while temp > 0:
            binary = str(temp % 2) + binary
            temp //= 2
        return binary

num = int(input("Enter a decimal number: "))
sol = Solution()
result = sol.decimal_to_binary(num)
print("Binary value:", result)
