""" Add an element to an Array
# 1. Define a class Solution.
# 2. Inside it, create a method add_element that takes an array arr and element x.
# 3. Initialize a new list result with length n+1.
# 4. Copy all elements of arr into result.
# 5. Set result[n] = x (append new element at the end).
# 6. Return result.
# 7. Take user input for array size.
# 8. Take user input for array elements.
# 9. Take user input for element to add.
# 10. Create a Solution object.
# 11. Call add_element and print result."""

class Solution:
    def add_element(self, arr: list, x: int) -> list:
        n = len(arr)
        result = [0] * (n + 1)
        for i in range(n):
            result[i] = arr[i]
        result[n] = x
        return result
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
x = int(input("Enter element to add: "))
sol = Solution()
result = sol.add_element(arr, x)
print("Array after adding element:", result)