""" # Explanation:
# 1. Define a class Solution.
# 2. Inside it, create a method first_non_repeating that takes a string s and returns a character or None.
# 3. Initialize an empty dictionary freq to store character counts.
# 4. Loop through each character in s to count frequencies (same as previous problem).
# 5. Loop through s again.
# 6. For each character, check if its frequency in freq is 1.
# 7. If found, return that character immediately (first non-repeating).
# 8. If no such character exists, return None.
# 9. Take user input for the string.
# 10. Create a Solution object.
# 11. Call first_non_repeating with the input.
# 12. Print the first non-repeating character (or indicate none found)."""

class Solution:
    def first_non_repeating(self, s: str):
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        for ch in s:
            if freq[ch] == 1:
                return ch
        return None
user_input = input("Enter a string: ")
sol = Solution()
result = sol.first_non_repeating(user_input)
if result:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found.")