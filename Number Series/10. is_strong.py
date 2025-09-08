""" Check if a number is a strong number or not
# 1. Define a class Solution.
# 2. Inside it, create a method is_strong that takes a number n.
# 3. Initialize sum_fact = 0, temp = n.
# 4. Loop while temp > 0:
#    - digit = temp % 10
#    - Calculate factorial of digit manually
#    - sum_fact += factorial
#    - temp //= 10
# 5. If sum_fact == n, return True, else False.
# 6. Take user input for number.
# 7. Create a Solution object.
# 8. Call is_strong and print result."""

class Solution:
    def is_strong(self, n: int) -> bool:
        def factorial(x: int) -> int:
            result = 1
            for i in range(1, x + 1):
                result *= i
            return result
        
        sum_fact = 0
        temp = n
        while temp > 0:
            digit = temp % 10
            sum_fact += factorial(digit)
            temp //= 10
        return sum_fact == n

num = int(input("Enter a number: "))
sol = Solution()
result = sol.is_strong(num)
print(f"Is {num} a Strong number?:", result)
