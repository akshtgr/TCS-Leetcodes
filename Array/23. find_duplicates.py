""" Find duplicates in O(n) time and O(1) extra space
# 1. Define a class Solution.
# 2. Inside it, create a method find_duplicates that takes an array arr where elements are in range 0 to n-1.
# 3. Loop through each element in arr:
#    - Increment arr[arr[i] % n] by n (mark occurrence).
# 4. Loop through arr again:
#    - If arr[i] // n > 1, i is a duplicate, add to result list.
# 5. Return the list of duplicates.
# 6. Take user input for array size.
# 7. Take user input for array elements.
# 8. Create a Solution object.
# 9. Call find_duplicates and print result."""

class Solution:
    def find_duplicates(self, arr: list) -> list:
        n = len(arr)
        result = []
        for i in range(n):
            arr[arr[i] % n] += n
        for i in range(n):
            if arr[i] // n > 1:
                result.append(i)
        return result
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements (0 to n-1): ").split()))
sol = Solution()
result = sol.find_duplicates(arr)
print("Duplicates in array:", result)