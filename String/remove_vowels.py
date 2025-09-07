""" # 1. Define a class Solution.
# 2. Inside it, create a method remove_vowels that takes a string s and returns a new string.
# 3. Define a string vowels containing all uppercase and lowercase vowels.
# 4. Initialize an empty result string.
# 5. Loop through each character in the input string s.
# 6. For each character, check if it is in vowels.
# 7. If it is not a vowel, append it to the result string.
# 8. After the loop, return the result string (which has no vowels).
# 9. Take user input for a string.
# 10. Create a Solution object.
# 11. Call remove_vowels on the user input.
# 12. Print the string without vowels."""

class Solution:
    def remove_vowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        result = ""
        for ch in s:
            if ch not in vowels:
                result += ch
        return result
user_input = input("Enter a string: ")
sol = Solution()
result = sol.remove_vowels(user_input)
print("String without vowels:", result)