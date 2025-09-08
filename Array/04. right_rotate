""" Print array after it is right rotated K times
# 1. Define a class Solution.
# 2. Inside it, create a method right_rotate that takes an array arr and number k.
# 3. Initialize an empty rotated array of same length as arr.
# 4. Loop through each index i in arr.
#    - Compute new_index = (i + k) % n (right rotation).
#    - Place arr[i] in rotated[new_index].
# 5. Return rotated array.
# 6. Take user input for array size.
# 7. Take user input for array elements.
# 8. Take user input for number of rotations k.
# 9. Create a Solution object.
# 10. Call right_rotate and print result."""

class Solution:
    def right_rotate(self, arr: list, k: int) -> list:
        n = len(arr)
        rotated = [0] * n
        for i in range(n):
            new_index = (i + k) % n
            rotated[new_index] = arr[i]
        return rotated
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter number of rotations: "))
sol = Solution()
result = sol.right_rotate(arr, k)
print("Array after right rotation:", result)