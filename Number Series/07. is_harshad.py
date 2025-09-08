""" Harshad (Or Niven) Number
# 1. Define a class Solution.
# 2. Inside it, create a method is_harshad that takes a number n.
# 3. Initialize sum_digits = 0, temp = n.
# 4. Loop while temp > 0:
#    - sum_digits += temp % 10
#    - temp //= 10
# 5. If n % sum_digits == 0, return True, else return False.
# 6. Take user input for number.
# 7. Create a Solution object.
# 8. Call is_harshad and print result."""

class Solution:
    def is_harshad(self, n: int) -> bool:
        sum_digits = 0
        temp = n
        while temp > 0:
            sum_digits += temp % 10
            temp //= 10
        return n % sum_digits == 0

num = int(input("Enter a number: "))
sol = Solution()
result = sol.is_harshad(num)
print(f"Is {num} a Harshad (Niven) number?:", result)
