""" Remove character
# 1. Define a class Solution.
# 2. Inside it, create a method remove_char that takes two inputs:
#    - s (the original string)
#    - ch (the character to remove).
# 3. Initialize an empty result string.
# 4. Loop through each character in s.
# 5. For each character, check if it is NOT equal to ch.
# 6. If it's not equal, append it to result.
# 7. After the loop ends, return the result string (with the character removed).
# 8. Take user input for the string.
# 9. Take user input for the character to remove.
# 10. Create a Solution object.
# 11. Call remove_char with both inputs.
# 12. Print the final string."""

class Solution:
    def remove_char(self, s: str, ch: str) -> str:
        result = ""
        for c in s:
            if c != ch:
                result += c
        return result
user_input = input("Enter a string: ")
char_to_remove = input("Enter the character to remove: ")
sol = Solution()
result = sol.remove_char(user_input, char_to_remove)
print("String after removing character:", result)