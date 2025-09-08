""" Program to find GCD or HCF of two numbers
# 1. Define a class Solution.
# 2. Inside it, create a method gcd that takes two numbers a and b.
# 3. Loop while b != 0:
#    - temp = b
#    - b = a % b
#    - a = temp
# 4. Return a (GCD).
# 5. Take user input for two numbers.
# 6. Create a Solution object.
# 7. Call gcd and print result."""

class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sol = Solution()
result = sol.gcd(a, b)
print("GCD of numbers:", result)
