""" Sum of numbers in string
# 1. Define a class Solution.
# 2. Inside it, create a method sum_of_numbers that takes a string s and returns an integer.
# 3. Initialize a variable total = 0 to store the sum of digits.
# 4. Loop through each character in s.
# 5. For each character, check if it is between '0' and '9'.
# 6. If true, convert it to its integer value by subtracting ASCII of '0' from ASCII of character.
# 7. Add this integer value to total.
# 8. After the loop ends, return the total sum.
# 9. Take user input for the string.
# 10. Create a Solution object.
# 11. Call sum_of_numbers with the input.
# 12. Print the sum of digits in the string."""

class Solution:
    def sum_of_numbers(self, s: str) -> int:
        total = 0
        for ch in s:
            if '0' <= ch <= '9':
                total += ord(ch) - ord('0')
        return total
user_input = input("Enter a string: ")
sol = Solution()
result = sol.sum_of_numbers(user_input)
print("Sum of digits in the string:", result)