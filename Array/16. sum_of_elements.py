""" Sum of elements in a given array
# 1. Define a class Solution.
# 2. Inside it, create a method sum_of_elements that takes an array arr.
# 3. Initialize total = 0.
# 4. Loop through each element in arr:
#    - Add element to total.
# 5. Return total after loop ends.
# 6. Take user input for array size.
# 7. Take user input for array elements.
# 8. Create a Solution object.
# 9. Call sum_of_elements and print result."""

class Solution:
    def sum_of_elements(self, arr: list) -> int:
        total = 0
        for num in arr:
            total += num
        return total
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
sol = Solution()
result = sol.sum_of_elements(arr)
print("Sum of elements in array:", result)