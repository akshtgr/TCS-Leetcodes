""" Convert a given number to words
# 1. Define a class Solution.
# 2. Inside it, create a method number_to_words that takes an integer n.
# 3. Create lists for single digits and tens.
# 4. Handle numbers from 0 to 99 manually.
# 5. For numbers >= 100, split into hundreds, tens, and ones and convert each part.
# 6. Concatenate words accordingly.
# 7. Take user input for number.
# 8. Create a Solution object.
# 9. Call number_to_words and print result."""

class Solution:
    def number_to_words(self, n: int) -> str:
        if n == 0:
            return "zero"

        ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
                 "sixteen", "seventeen", "eighteen", "nineteen"]
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        words = ""
        if n >= 100:
            words += ones[n // 100] + " hundred"
            n %= 100
            if n > 0:
                words += " and "
        if 10 <= n <= 19:
            words += teens[n - 10]
        else:
            if n >= 20:
                words += tens[n // 10]
                n %= 10
                if n > 0:
                    words += "-" + ones[n]
            else:
                if n > 0:
                    words += ones[n]
        return words

num = int(input("Enter a number (0-999): "))
sol = Solution()
result = sol.number_to_words(num)
print("Number in words:", result)
