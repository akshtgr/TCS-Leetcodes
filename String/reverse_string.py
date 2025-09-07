""" # Explanation:
# 1. Define a class Solution.
# 2. Inside it, create a method reverse_string that takes a string s and returns a new string.
# 3. Initialize an empty result string.
# 4. Loop through s from the last character to the first using a while loop and index.
# 5. Append each character to the result string.
# 6. After the loop ends, return the reversed string.
# 7. Take user input for the string.
# 8. Create a Solution object.
# 9. Call reverse_string with the input.
# 10. Print the reversed string."""

class Solution:
    def reverse_string(self, s: str) -> str:
        result = ""
        i = len(s) - 1
        while i >= 0:
            result += s[i]
            i -= 1
        return result
user_input = input("Enter a string: ")
sol = Solution()
result = sol.reverse_string(user_input)
print("Reversed string:", result)