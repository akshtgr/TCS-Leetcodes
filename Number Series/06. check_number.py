""" Number is Positive, Negative, Odd, Even, Zero
# 1. Define a class Solution.
# 2. Inside it, create a method check_number that takes a number n.
# 3. Initialize a list result.
# 4. Check if n == 0: append "Zero".
# 5. Else, check if n > 0: append "Positive", else append "Negative".
# 6. Check if n % 2 == 0: append "Even", else append "Odd".
# 7. Return result.
# 8. Take user input for number.
# 9. Create a Solution object.
# 10. Call check_number and print result."""

class Solution:
    def check_number(self, n: int) -> list:
        result = []
        if n == 0:
            result.append("Zero")
        else:
            if n > 0:
                result.append("Positive")
            else:
                result.append("Negative")
            if n % 2 == 0:
                result.append("Even")
            else:
                result.append("Odd")
        return result

num = int(input("Enter a number: "))
sol = Solution()
result = sol.check_number(num)
print("Properties of number:", result)
