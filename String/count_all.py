""" # Explanation:
# 1. Define a class Solution.
# 2. Inside it, create a method count_all that takes a string s and returns a tuple (vowels, consonants, digits, specials).
# 3. Define a string vowels containing all uppercase and lowercase vowels.
# 4. Define a string digits containing '0' to '9'.
# 5. Initialize counters: vowel_count, consonant_count, digit_count, special_count to 0.
# 6. Loop through each character in s.
#    - If character is in vowels, increment vowel_count.
#    - Else if character is in digits, increment digit_count.
#    - Else if character is between 'a'-'z' or 'A'-'Z', increment consonant_count.
#    - Else, increment special_count.
# 7. After loop ends, return the four counts as a tuple.
# 8. Take user input for the string.
# 9. Create a Solution object.
# 10. Call count_all with input and print each count."""

class Solution:
    def count_all(self, s: str) -> tuple:
        vowels = "aeiouAEIOU"
        digits = "0123456789"
        vowel_count = 0
        consonant_count = 0
        digit_count = 0
        special_count = 0
        
        for ch in s:
            if ch in vowels:
                vowel_count += 1
            elif ch in digits:
                digit_count += 1
            elif ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
                consonant_count += 1
            else:
                special_count += 1
        return (vowel_count, consonant_count, digit_count, special_count)

user_input = input("Enter a string: ")
sol = Solution()
v, c, d, sp = sol.count_all(user_input)
print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Special characters:", sp)
