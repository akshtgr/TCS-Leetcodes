""" Find maximum possible stolen value from houses
# 1. Define a class Solution.
# 2. Inside it, create a method max_stolen_value that takes an array arr of house values.
# 3. Use dynamic programming approach iteratively (brute force):
#    - If no houses, return 0.
#    - Initialize two variables: prev1 = 0, prev2 = 0.
#    - Loop through each house value:
#        - current = max(prev1, prev2 + value)
#        - Update prev2 = prev1, prev1 = current
# 4. Return prev1 as maximum stolen value.
# 5. Take user input for number of houses.
# 6. Take user input for house values.
# 7. Create a Solution object.
# 8. Call max_stolen_value and print result."""

class Solution:
    def max_stolen_value(self, arr: list) -> int:
        prev1, prev2 = 0, 0
        for value in arr:
            current = max(prev1, prev2 + value)
            prev2 = prev1
            prev1 = current
        return prev1
n = int(input("Enter number of houses: "))
arr = list(map(int, input("Enter values of houses: ").split()))
sol = Solution()
result = sol.max_stolen_value(arr)
print("Maximum possible stolen value:", result)