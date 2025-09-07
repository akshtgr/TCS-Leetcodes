""" Reverse words in a given string
# 1. Define a class Solution.
# 2. Inside it, create a method reverse_words that takes a string s and returns a new string.
# 3. Initialize an empty list words to store individual words and an empty string word.
# 4. Loop through each character in s.
#    - If character is not a space, add it to word.
#    - If character is a space and word is not empty, append word to words list and reset word.
# 5. After loop, append last word if not empty.
# 6. Initialize an empty string result.
# 7. Loop through words list in reverse order, appending each word and a space.
# 8. Remove trailing space and return result.
# 9. Take user input for the string.
# 10. Create a Solution object.
# 11. Call reverse_words with input and print result."""

class Solution:
    def reverse_words(self, s: str) -> str:
        words = []
        word = ""
        for ch in s:
            if ch != " ":
                word += ch
            else:
                if word:
                    words.append(word)
                    word = ""
        if word:
            words.append(word)
        result = ""
        for i in range(len(words)-1, -1, -1):
            result += words[i] + " "
        return result.strip()
user_input = input("Enter a string: ")
sol = Solution()
result = sol.reverse_words(user_input)
print("Reversed words string:", result)