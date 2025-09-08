""" Program for array rotation
# 1. Define a class Solution.
# 2. Inside it, create a method rotate_array that takes an array arr and a number d (steps to rotate).
# 3. Initialize an empty list rotated of same length as arr.
# 4. Loop through each index i in arr.
#    - Compute new_index = (i - d) % n (left rotation).
#    - Place arr[i] in rotated[new_index].
# 5. Return rotated list.
# 6. Take user input for array size.
# 7. Take user input for array elements.
# 8. Take user input for rotation steps d.
# 9. Create a Solution object.
# 10. Call rotate_array and print result."""

class Solution:
    def rotate_array(self, arr: list, d: int) -> list:
        n = len(arr)
        rotated = [0] * n
        for i in range(n):
            new_index = (i - d) % n
            rotated[new_index] = arr[i]
        return rotated
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
d = int(input("Enter number of rotations: "))
sol = Solution()
result = sol.rotate_array(arr, d)
print("Array after rotation:", result)