""" ASCII Value of a character	
# Define a class named Solution as per LeetCode-style structure.
# Define a method ascii_value that takes a string s and returns an integer.
# We'll assume s is a single character.
# Convert the character into its ASCII value using the ord() function.
# ord() gives the Unicode code point of the character.
# Return the integer value (ASCII code).
# Prompt the user to enter a character and read it into user_input.
# Create an instance of the Solution class.
# Call the ascii_value method with the user input and store the result.
# Print the ASCII value of the entered character."""

class Solution:
    def ascii_value(self, s: str) -> int:
        value = ord(s)
        return value
user_input = input("Enter a single character: ")
sol = Solution()
result = sol.ascii_value(user_input)
print("ASCII Value:", result)