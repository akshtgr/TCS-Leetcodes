""" Smallest and second smallest elements in an array
# 1. Define a class Solution.
# 2. Inside it, create a method two_smallest that takes an array arr.
# 3. Initialize smallest and second_smallest as infinity (a very large number).
# 4. Loop through each element in arr:
#    - If current element < smallest:
#         second_smallest = smallest
#         smallest = current element
#    - Else if current element < second_smallest and not equal to smallest:
#         second_smallest = current element
# 5. If second_smallest is still infinity, return -1 (no second smallest exists).
# 6. Otherwise, return (smallest, second_smallest).
# 7. Take user input for array size.
# 8. Take user input for array elements.
# 9. Create a Solution object.
# 10. Call two_smallest and print results."""

class Solution:
    def two_smallest(self, arr: list) -> tuple:
        smallest = float('inf')
        second_smallest = float('inf')
        for num in arr:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest and num != smallest:
                second_smallest = num
        
        if second_smallest == float('inf'):
            return -1
        return (smallest, second_smallest)
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
sol = Solution()
result = sol.two_smallest(arr)
print("Smallest and second smallest elements:", result)