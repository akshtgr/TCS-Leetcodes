""" Capitalize first and last character of each word 
# 1. Define a class Solution.
# 2. Inside it, create a method capitalize_first_last that takes a string s and returns a new string.
# 3. Initialize an empty result string and an empty word string.
# 4. Loop through each character in s.
# 5. If the character is not a space, keep adding it to the current word.
# 6. If the character is a space, process the word:
#    - If the word length is 1, capitalize it.
#    - If the word length > 1, capitalize first and last characters, keep middle same.
#    - Append processed word and a space to result.
#    - Reset word to empty.
# 7. After the loop, process the last word (same logic as step 6).
# 8. Return the final result string.
# 9. Take user input for the string.
# 10. Create a Solution object.
# 11. Call capitalize_first_last with the input.
# 12. Print the modified string."""

class Solution:
    def capitalize_first_last(self, s: str) -> str:
        result = ""
        word = ""
        for ch in s:
            if ch != " ":
                word += ch
            else:
                if len(word) == 1:
                    result += word.upper()
                elif len(word) > 1:
                    result += word[0].upper() + word[1:-1] + word[-1].upper()
                result += " "
                word = ""
        if len(word) == 1:
            result += word.upper()
        elif len(word) > 1:
            result += word[0].upper() + word[1:-1] + word[-1].upper()
        return result
user_input = input("Enter a string: ")
sol = Solution()
result = sol.capitalize_first_last(user_input)
print("Modified string:", result)