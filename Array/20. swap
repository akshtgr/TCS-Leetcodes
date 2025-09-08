""" Block swap algorithm for array rotation (left rotation)
# 1. Define a class Solution.
# 2. Inside it, create a method left_rotate that takes an array arr and number d (rotations).
# 3. Normalize d = d % n (to avoid unnecessary full rotations).
# 4. Define a helper function swap to swap blocks of size k between two parts of array.
# 5. Implement recursive block swap approach:
#    - If d == 0 or d == n, return arr (no rotation needed).
#    - If d == n - d, swap first d elements with last d elements.
#    - If d < n - d, swap first d elements with last d elements of same size, recurse on remaining array.
#    - Else, swap last n-d elements with first n-d elements of same size, recurse.
# 6. Return rotated array.
# 7. Take user input for array size.
# 8. Take user input for array elements.
# 9. Take user input for rotation count d.
# 10. Create a Solution object.
# 11. Call left_rotate and print result."""

class Solution:
    def swap(self, arr, fi, si, k):
        for i in range(k):
            arr[fi + i], arr[si + i] = arr[si + i], arr[fi + i]
    def left_rotate_util(self, arr, d, n):
        if d == 0 or d == n:
            return
        if d == n - d:
            self.swap(arr, 0, n - d, d)
            return
        if d < n - d:
            self.swap(arr, 0, n - d, d)
            self.left_rotate_util(arr, d, n - d)
        else:
            self.swap(arr, 0, d, n - d)
            self.left_rotate_util(arr[n - d:], 2 * d - n, d)
    def left_rotate(self, arr: list, d: int) -> list:
        n = len(arr)
        d = d % n
        self.left_rotate_util(arr, d, n)
        return arr
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
d = int(input("Enter number of rotations: "))
sol = Solution()
result = sol.left_rotate(arr, d)
print("Array after left rotation:", result)