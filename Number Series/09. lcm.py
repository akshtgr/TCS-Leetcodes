""" LCM of two numbers
# 1. Define a class Solution.
# 2. Inside it, create a method lcm that takes two numbers a and b.
# 3. Calculate LCM using formula: lcm = (a * b) // gcd(a, b)
# 4. Use previously defined gcd method.
# 5. Return lcm.
# 6. Take user input for two numbers.
# 7. Create a Solution object.
# 8. Call lcm and print result."""

class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a

    def lcm(self, a: int, b: int) -> int:
        return (a * b) // self.gcd(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sol = Solution()
result = sol.lcm(a, b)
print("LCM of numbers:", result)
