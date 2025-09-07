""" Remove duplicates from a given string
# 1. Define a class Solution.
# 2. Inside it, create a method remove_duplicates that takes a string s and returns a new string.
# 3. Initialize an empty result string.
# 4. Loop through each character in s.
# 5. For each character, check if it is not already in result.
# 6. If not, append it to result.
# 7. After loop ends, return result string (duplicates removed).
# 8. Take user input for the string.
# 9. Create a Solution object.
# 10. Call remove_duplicates with input and print result."""

class Solution:
    def remove_duplicates(self, s: str) -> str:
        result = ""
        for ch in s:
            if ch not in result:
                result += ch
        return result
user_input = input("Enter a string: ")
sol = Solution()
result = sol.remove_duplicates(user_input)
print("String after removing duplicates:", result)