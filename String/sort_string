""" # Explanation:
# 1. Define a class Solution.
# 2. Inside it, create a method sort_string that takes a string s and returns a new string.
# 3. Convert the string s to a list of characters (for easier swapping).
# 4. Use a simple brute-force sorting algorithm (like bubble sort) to sort the characters.
# 5. Loop through each character and compare with subsequent characters, swapping if out of order.
# 6. After sorting, join the list back into a string.
# 7. Return the sorted string.
# 8. Take user input for the string.
# 9. Create a Solution object.
# 10. Call sort_string with the input and print result."""

class Solution:
    def sort_string(self, s: str) -> str:
        chars = list(s)
        n = len(chars)
        for i in range(n):
            for j in range(i+1, n):
                if chars[i] > chars[j]:
                    chars[i], chars[j] = chars[j], chars[i]
        return "".join(chars)
user_input = input("Enter a string: ")
sol = Solution()
result = sol.sort_string(user_input)
print("Sorted string:", result)