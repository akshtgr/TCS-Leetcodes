""" # Define a class named Solution to match the LeetCode-style structure.
# Define a method is_palindrome that takes a string s and returns a boolean.
# Initialize the left pointer i to the start index 0.
# Initialize the right pointer j to the last index of s (length - 1).
# Loop while the left pointer is less than the right pointer.
# If the character at index i is not equal to the character at index j...
# ...then s is not a palindrome; return False immediately.
# Move the left pointer one step to the right.
# Move the right pointer one step to the left.
# If we finished the loop without mismatches, the string is a palindrome; return True.
# Prompt the user to enter a string and read it into user_input.
# Create an instance of the Solution class.
# Call the is_palindrome method with the user input and store the boolean result.
# Print the result in a human-readable form."""

class Solution:
    def is_palindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
user_input = input("Enter a string to check if it's a palindrome: ")
sol = Solution()
result = sol.is_palindrome(user_input)
print("Palindrome:", result)