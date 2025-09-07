""" # Explanation:
# 1. Define a class Solution.
# 2. Inside it, create a method char_frequency that takes a string s and returns a dictionary.
# 3. Initialize an empty dictionary freq to store character counts.
# 4. Loop through each character in s.
# 5. For each character, check if it is already in freq.
#    - If yes, increment its count by 1.
#    - If no, add it to freq with count 1.
# 6. After the loop ends, return the dictionary freq.
# 7. Take user input for the string.
# 8. Create a Solution object.
# 9. Call char_frequency with the input.
# 10. Print the frequency dictionary."""

class Solution:
    def char_frequency(self, s: str) -> dict:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        return freq
user_input = input("Enter a string: ")
sol = Solution()
result = sol.char_frequency(user_input)
print("Character frequency:", result)