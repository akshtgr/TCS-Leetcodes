""" One string contains wildcard characters
# 1. Define a class Solution.
# 2. Inside it, create a method match_wildcard that takes two strings s and pattern and returns a boolean.
# 3. '*' in pattern can match any sequence of characters (including empty), '?' matches any single character.
# 4. Implement a recursive brute-force approach:
#    - If both strings are empty, return True.
#    - If pattern is empty but s is not, return False.
#    - If current pattern character is '?', move both pointers forward recursively.
#    - If current pattern character is '*', try two possibilities recursively:
#        a) '*' matches 0 characters (move pattern forward)
#        b) '*' matches 1 or more characters (move s forward)
#    - If current characters match, move both pointers forward recursively.
#    - Otherwise, return False.
# 5. Take user input for the string and the pattern.
# 6. Create a Solution object.
# 7. Call match_wildcard with inputs and print result."""

class Solution:
    def match_wildcard(self, s: str, pattern: str) -> bool:
        def helper(i, j):
            if i == len(s) and j == len(pattern):
                return True
            if j == len(pattern):
                return False
            if j < len(pattern) and pattern[j] == '*':
                return helper(i, j+1) or (i < len(s) and helper(i+1, j))
            if i < len(s) and (pattern[j] == '?' or s[i] == pattern[j]):
                return helper(i+1, j+1)
            return False
        return helper(0, 0)
s = input("Enter the string: ")
pattern = input("Enter the pattern (with ? and *): ")
sol = Solution()
result = sol.match_wildcard(s, pattern)
print("Does string match the pattern?:", result)