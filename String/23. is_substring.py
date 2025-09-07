""" Check if a string is substring of another
# 1. Define a class Solution.
# 2. Inside it, create a method is_substring that takes two strings: text and pattern.
# 3. Get the lengths of text (n) and pattern (m).
# 4. Loop through text from index 0 to n-m.
# 5. For each index, compare substring of length m with pattern character by character.
# 6. If all characters match, return True (pattern is a substring).
# 7. If loop ends without match, return False.
# 8. Take user input for the text string.
# 9. Take user input for the pattern string.
# 10. Create a Solution object.
# 11. Call is_substring with inputs and print result."""

class Solution:
    def is_substring(self, text: str, pattern: str) -> bool:
        n = len(text)
        m = len(pattern)
        for i in range(n - m + 1):
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return True
        return False
text = input("Enter the main string: ")
pattern = input("Enter the substring to check: ")
sol = Solution()
result = sol.is_substring(text, pattern)
print("Is substring?:", result)