""" Area of a circle
# 1. Define a class Solution.
# 2. Inside it, create a method area_circle that takes radius r.
# 3. Use formula: area = 3.141592653589793 * r * r
# 4. Return area.
# 5. Take user input for radius.
# 6. Create a Solution object.
# 7. Call area_circle and print result."""

class Solution:
    def area_circle(self, r: float) -> float:
        pi = 3.141592653589793
        return pi * r * r

radius = float(input("Enter radius of circle: "))
sol = Solution()
result = sol.area_circle(radius)
print("Area of the circle:", result)
