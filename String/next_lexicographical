""" # Explanation:
# 1. Define a class Solution.
# 2. Inside it, create a method next_lexicographical that takes a string s and returns the next lexicographical string.
# 3. Convert string s to a list of characters for manipulation.
# 4. Start from the end of the list and find the first character that is smaller than its next character (pivot).
# 5. If no such pivot exists, return "No next string" (string is highest lexicographically).
# 6. Find the smallest character on the right of pivot that is greater than pivot.
# 7. Swap pivot and that character.
# 8. Reverse the substring to the right of pivot index.
# 9. Join the list back into a string and return it.
# 10. Take user input for the string.
# 11. Create a Solution object.
# 12. Call next_lexicographical with input and print result."""

class Solution:
    def next_lexicographical(self, s: str) -> str:
        chars = list(s)
        n = len(chars)
        i = n - 2
        while i >= 0 and chars[i] >= chars[i + 1]:
            i -= 1
        if i == -1:
            return "No next string"
        j = n - 1
        while chars[j] <= chars[i]:
            j -= 1
        chars[i], chars[j] = chars[j], chars[i]
        chars[i + 1:] = chars[i + 1:][::-1]
        return "".join(chars)
user_input = input("Enter a string: ")
sol = Solution()
result = sol.next_lexicographical(user_input)
print("Next lexicographical string:", result)