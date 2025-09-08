""" Check if a given year is leap year
# 1. Define a class Solution.
# 2. Inside it, create a method is_leap_year that takes year y.
# 3. If y % 400 == 0, return True
# 4. Else if y % 100 == 0, return False
# 5. Else if y % 4 == 0, return True
# 6. Else return False
# 7. Take user input for year.
# 8. Create a Solution object.
# 9. Call is_leap_year and print result."""

class Solution:
    def is_leap_year(self, y: int) -> bool:
        if y % 400 == 0:
            return True
        elif y % 100 == 0:
            return False
        elif y % 4 == 0:
            return True
        else:
            return False

year = int(input("Enter a year: "))
sol = Solution()
result = sol.is_leap_year(year)
print(f"Is {year} a leap year?:", result)
