""" Duplicates in the input string
# 1. Define a class Solution.
# 2. Inside it, create a method find_duplicates that takes a string s and returns a string of duplicates.
# 3. Initialize an empty dictionary freq to count character occurrences.
# 4. Loop through each character in s.
#    - If character is in freq, increment its count.
#    - Otherwise, set its count to 1.
# 5. Initialize an empty string duplicates to store repeated characters.
# 6. Loop through freq, and if the count of a character > 1, append it to duplicates.
# 7. Return duplicates string.
# 8. Take user input for the string.
# 9. Create a Solution object.
# 10. Call find_duplicates with input and print result."""

class Solution:
    def find_duplicates(self, s: str) -> str:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        duplicates = ""
        for ch in freq:
            if freq[ch] > 1:
                duplicates += ch
        return duplicates
user_input = input("Enter a string: ")
sol = Solution()
result = sol.find_duplicates(user_input)
print("Duplicate characters:", result)