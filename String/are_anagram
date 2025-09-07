""" # Explanation:
# 1. Define a class Solution.
# 2. Inside it, create a method are_anagrams that takes two strings s1 and s2 and returns a boolean.
# 3. If lengths of s1 and s2 are different, immediately return False.
# 4. Initialize two dictionaries freq1 and freq2 to store character frequencies of s1 and s2.
# 5. Loop through s1 and populate freq1.
# 6. Loop through s2 and populate freq2.
# 7. Loop through each character in freq1:
#    - If character not in freq2 or counts don't match, return False.
# 8. Return True if all characters match in frequency.
# 9. Take user input for both strings.
# 10. Create a Solution object.
# 11. Call are_anagrams with inputs and print result."""

class Solution:
    def are_anagrams(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        freq1 = {}
        freq2 = {}
        for ch in s1:
            if ch in freq1:
                freq1[ch] += 1
            else:
                freq1[ch] = 1
        for ch in s2:
            if ch in freq2:
                freq2[ch] += 1
            else:
                freq2[ch] = 1
        for ch in freq1:
            if ch not in freq2 or freq1[ch] != freq2[ch]:
                return False
        return True
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
sol = Solution()
result = sol.are_anagrams(string1, string2)
print("Are the strings anagrams?:", result)