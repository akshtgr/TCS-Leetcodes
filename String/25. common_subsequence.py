""" Common subsequence in two strings
# 1. Define a class Solution.
# 2. Inside it, create a method common_subsequence that takes two strings s1 and s2 and returns a string.
# 3. Initialize an empty string result.
# 4. Loop through each character in s1.
# 5. For each character, check if it exists in s2.
#    - If yes, append it to result and remove the first occurrence from s2 to avoid duplicate counting.
# 6. After the loop ends, return result string (common subsequence in order of s1).
# 7. Take user input for the first string.
# 8. Take user input for the second string.
# 9. Create a Solution object.
# 10. Call common_subsequence with inputs and print result."""

class Solution:
    def common_subsequence(self, s1: str, s2: str) -> str:
        result = ""
        s2_list = list(s2)
        for ch in s1:
            for i in range(len(s2_list)):
                if ch == s2_list[i]:
                    result += ch
                    s2_list[i] = ""  # remove used character
                    break
        return result
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
sol = Solution()
result = sol.common_subsequence(s1, s2)
print("Common subsequence:", result)