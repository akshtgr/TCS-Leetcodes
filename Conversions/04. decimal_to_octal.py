""" Convert Decimal to Octal
# 1. Define a class Solution.
# 2. Inside it, create a method decimal_to_octal that takes a decimal number n.
# 3. Initialize octal = "", temp = n.
# 4. Loop while temp > 0:
#    - octal = str(temp % 8) + octal
#    - temp //= 8
# 5. Handle case n = 0 separately.
# 6. Return octal string.
# 7. Take user input for decimal number.
# 8. Create a Solution object.
# 9. Call decimal_to_octal and print result."""

class Solution:
    def decimal_to_octal(self, n: int) -> str:
        if n == 0:
            return "0"
        octal = ""
        temp = n
        while temp > 0:
            octal = str(temp % 8) + octal
            temp //= 8
        return octal

num = int(input("Enter a decimal number: "))
sol = Solution()
result = sol.decimal_to_octal(num)
print("Octal value:", result)
