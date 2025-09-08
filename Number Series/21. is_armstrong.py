""" Armstrong Numbers
# 1. Define a class Solution.
# 2. Inside it, create a method is_armstrong that takes a number n.
# 3. Convert n to string to find number of digits.
# 4. Initialize sum_pow = 0.
# 5. Loop through each digit in n:
#    - sum_pow += int(digit) ** number_of_digits
# 6. If sum_pow == n, return True, else False.
# 7. Take user input for number.
# 8. Create a Solution object.
# 9. Call is_armstrong and print result."""

class Solution:
    def is_armstrong(self, n: int) -> bool:
        num_str = str(n)
        num_digits = len(num_str)
        sum_pow = 0
        for digit in num_str:
            sum_pow += int(digit) ** num_digits
        return sum_pow == n

num = int(input("Enter a number: "))
sol = Solution()
result = sol.is_armstrong(num)
print(f"Is {num} an Armstrong Number?:", result)