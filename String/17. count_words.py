""" Count words in a given string
# 1. Define a class Solution.
# 2. Inside it, create a method count_words that takes a string s and returns an integer.
# 3. Initialize variables count = 0 and in_word = False to track words.
# 4. Loop through each character in s.
# 5. If the character is not a space and in_word is False, increment count and set in_word = True.
# 6. If the character is a space, set in_word = False.
# 7. After the loop ends, return count.
# 8. Take user input for the string.
# 9. Create a Solution object.
# 10. Call count_words with input and print result."""

class Solution:
    def count_words(self, s: str) -> int:
        count = 0
        in_word = False
        for ch in s:
            if ch != " " and not in_word:
                count += 1
                in_word = True
            elif ch == " ":
                in_word = False
        return count
user_input = input("Enter a string: ")
sol = Solution()
result = sol.count_words(user_input)
print("Number of words in the string:", result)