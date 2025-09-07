""" Remove all characters other than alphabets	
# 1. Define a class Solution.
# 2. Inside it, create a method remove_non_alpha that takes a string s and returns a new string.
# 3. Initialize an empty result string.
# 4. Loop through each character in s.
# 5. For each character, check if it lies in the range of 'a' to 'z' or 'A' to 'Z'.
# 6. If the condition is true, append the character to result.
# 7. After the loop ends, return the result string (which has only alphabets).
# 8. Take user input for the string.
# 9. Create a Solution object.
# 10. Call remove_non_alpha with the input.
# 11. Print the final string with only alphabets."""

class Solution:
    def remove_non_alpha(self, s: str) -> str:
        result = ""
        for ch in s:
            if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
                result += ch
        return result
user_input = input("Enter a string: ")
sol = Solution()
result = sol.remove_non_alpha(user_input)
print("String with only alphabets:", result)