""" Primitive Abundant Number
# 1. Define a class Solution.
# 2. Inside it, create a method is_primitive_abundant that takes a number n.
# 3. Check if n is abundant (sum of proper divisors > n).
# 4. Loop i from 1 to n-1:
#    - If n % i == 0 and i is abundant, return False
# 5. If n is abundant and no proper divisor is abundant, return True.
# 6. Take user input for number.
# 7. Create a Solution object.
# 8. Call is_primitive_abundant and print result."""

class Solution:
    def is_abundant(self, n: int) -> bool:
        sum_div = 0
        for i in range(1, n):
            if n % i == 0:
                sum_div += i
        return sum_div > n

    def is_primitive_abundant(self, n: int) -> bool:
        if not self.is_abundant(n):
            return False
        for i in range(1, n):
            if n % i == 0 and self.is_abundant(i):
                return False
        return True

num = int(input("Enter a number: "))
sol = Solution()
result = sol.is_primitive_abundant(num)
print(f"Is {num} a Primitive Abundant Number?:", result)
