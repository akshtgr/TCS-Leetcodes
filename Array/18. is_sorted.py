""" Program to check if an array is sorted or not
# 1. Define a class Solution.
# 2. Inside it, create a method is_sorted that takes an array arr.
# 3. Loop through the array from index 1 to end:
#    - If arr[i] < arr[i-1], return False (array is not sorted).
# 4. If loop finishes without returning False, return True.
# 5. Take user input for array size.
# 6. Take user input for array elements.
# 7. Create a Solution object.
# 8. Call is_sorted and print result."""

class Solution:
    def is_sorted(self, arr: list) -> bool:
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
sol = Solution()
result = sol.is_sorted(arr)
print("Is array sorted?:", result)