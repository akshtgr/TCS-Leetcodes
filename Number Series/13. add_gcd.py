""" Program to add two fractions
# 1. Define a class Solution.
# 2. Inside it, create a method add_fractions that takes four integers: num1, den1, num2, den2.
# 3. Calculate common denominator = den1 * den2.
# 4. Calculate numerator = num1 * den2 + num2 * den1.
# 5. Find GCD of numerator and denominator to simplify fraction.
# 6. Return simplified numerator and denominator.
# 7. Take user input for two fractions.
# 8. Create a Solution object.
# 9. Call add_fractions and print result."""

class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

    def add_fractions(self, num1: int, den1: int, num2: int, den2: int) -> tuple:
        numerator = num1 * den2 + num2 * den1
        denominator = den1 * den2
        common = self.gcd(numerator, denominator)
        return (numerator // common, denominator // common)

num1 = int(input("Enter numerator of first fraction: "))
den1 = int(input("Enter denominator of first fraction: "))
num2 = int(input("Enter numerator of second fraction: "))
den2 = int(input("Enter denominator of second fraction: "))
sol = Solution()
result = sol.add_fractions(num1, den1, num2, den2)
print("Sum of fractions (simplified):", result[0], "/", result[1])
