""" # Explanation:
# 1. Define a class Solution.
# 2. Inside it, create a method encrypt_string that takes a string s and returns a new string.
# 3. Initialize an empty result string.
# 4. Loop through each character in s.
# 5. If character is between 'a' and 'y' or 'A' and 'Y', shift ASCII by +1 and append.
# 6. If character is 'z', change to 'a'; if 'Z', change to 'A'.
# 7. If character is not an alphabet, append it as is.
# 8. After loop ends, return result string.
# 9. Take user input for the string.
# 10. Create a Solution object.
# 11. Call encrypt_string with input and print result."""

class Solution:
    def encrypt_string(self, s: str) -> str:
        result = ""
        for ch in s:
            if 'a' <= ch <= 'y' or 'A' <= ch <= 'Y':
                result += chr(ord(ch) + 1)
            elif ch == 'z':
                result += 'a'
            elif ch == 'Z':
                result += 'A'
            else:
                result += ch
        return result
user_input = input("Enter a string: ")
sol = Solution()
result = sol.encrypt_string(user_input)
print("Encrypted string:", result)