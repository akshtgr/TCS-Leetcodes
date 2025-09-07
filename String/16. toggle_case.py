""" Convert characters of a string to opposite case
# 1. Define a class Solution.
# 2. Inside it, create a method toggle_case that takes a string s and returns a new string.
# 3. Initialize an empty result string.
# 4. Loop through each character in s.
# 5. If character is between 'a' and 'z', convert to uppercase by subtracting 32 from ASCII and append to result.
# 6. If character is between 'A' and 'Z', convert to lowercase by adding 32 to ASCII and append to result.
# 7. If character is not an alphabet, append it as is.
# 8. After loop ends, return the result string.
# 9. Take user input for the string.
# 10. Create a Solution object.
# 11. Call toggle_case with input and print result."""

class Solution:
    def toggle_case(self, s: str) -> str:
        result = ""
        for ch in s:
            if 'a' <= ch <= 'z':
                result += chr(ord(ch) - 32)
            elif 'A' <= ch <= 'Z':
                result += chr(ord(ch) + 32)
            else:
                result += ch
        return result
user_input = input("Enter a string: ")
sol = Solution()
result = sol.toggle_case(user_input)
print("String with toggled case:", result)