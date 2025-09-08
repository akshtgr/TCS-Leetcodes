""" Palindromes in a given range
# 1. Define a class Solution.
# 2. Inside it, create a method palindromes_in_range that takes start and end.
# 3. Initialize empty list result.
# 4. Loop num from start to end:
#    - Check if str(num) reversed equals str(num)
#    - If yes, append num to result
# 5. Return result.
# 6. Take user input for start and end of range.
# 7. Create a Solution object.
# 8. Call palindromes_in_range and print result."""

class Solution:
    def palindromes_in_range(self, start: int, end: int) -> list:
        result = []
        for num in range(start, end + 1):
            if str(num) == str(num)[::-1]:
                result.append(num)
        return result

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
sol = Solution()
result = sol.palindromes_in_range(start, end)
print("Palindromes in range:", result)
