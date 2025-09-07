""" # Explanation:
# 1. Define a class Solution.
# 2. Inside it, create a method remove_brackets that takes a string s and returns a new string.
# 3. Initialize an empty result string.
# 4. Loop through each character in s.
# 5. If the character is not '(', ')', '[', ']', '{', or '}', append it to result.
# 6. After loop ends, return result string (with all brackets removed).
# 7. Take user input for the string.
# 8. Create a Solution object.
# 9. Call remove_brackets with input and print result."""

class Solution:
    def remove_brackets(self, s: str) -> str:
        result = ""
        for ch in s:
            if ch not in "({[]})":
                result += ch
        return result
user_input = input("Enter an algebraic expression: ")
sol = Solution()
result = sol.remove_brackets(user_input)
print("Expression without brackets:", result)