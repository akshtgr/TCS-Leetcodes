""" Roots of Quadratic equation
# 1. Define a class Solution.
# 2. Inside it, create a method roots that takes coefficients a, b, c.
# 3. Calculate discriminant D = b*b - 4*a*c
# 4. If D > 0: two real roots, calculate using (-b ± sqrt(D)) / (2*a)
# 5. If D == 0: one real root -b / (2*a)
# 6. If D < 0: complex roots
# 7. Return roots accordingly.
# 8. Take user input for a, b, c.
# 9. Create a Solution object.
# 10. Call roots and print result."""

class Solution:
    def roots(self, a: float, b: float, c: float) -> tuple:
        D = b*b - 4*a*c
        if D > 0:
            root1 = (-b + D**0.5) / (2*a)
            root2 = (-b - D**0.5) / (2*a)
            return (root1, root2)
        elif D == 0:
            root = -b / (2*a)
            return (root,)
        else:
            real = -b / (2*a)
            imag = (abs(D)**0.5) / (2*a)
            return (complex(real, imag), complex(real, -imag))

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
sol = Solution()
result = sol.roots(a, b, c)
print("Roots of quadratic equation:", result)
