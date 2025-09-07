""" # Explanation:
# 1. Define a class Solution.
# 2. Inside it, create a method smallest_largest_word that takes a string s and returns a tuple (smallest, largest).
# 3. Initialize an empty list words to store individual words.
# 4. Initialize an empty string word to accumulate characters for the current word.
# 5. Loop through each character in s.
#    - If the character is not a space, add it to word.
#    - If it is a space and word is not empty, append word to words list and reset word.
# 6. After loop, check if last word exists and append it.
# 7. Initialize smallest and largest as the first word.
# 8. Loop through words to find the word with minimum length (smallest) and maximum length (largest).
# 9. Return the tuple (smallest, largest).
# 10. Take user input for the string.
# 11. Create a Solution object.
# 12. Call smallest_largest_word with input and print results."""

class Solution:
    def smallest_largest_word(self, s: str) -> tuple:
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
        if not words:
            return ("", "")
        smallest = largest = words[0]
        for w in words:
            if len(w) < len(smallest):
                smallest = w
            if len(w) > len(largest):
                largest = w
        return (smallest, largest)
user_input = input("Enter a string: ")
sol = Solution()
smallest, largest = sol.smallest_largest_word(user_input)
print("Smallest word:", smallest)
print("Largest word:", largest)