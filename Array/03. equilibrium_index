""" Equilibrium index of an array
# 1. Define a class Solution.
# 2. Inside it, create a method equilibrium_index that takes an array arr and returns the index.
# 3. Loop through each index i in arr.
# 4. For each index i:
#    - Compute left_sum = sum of elements from index 0 to i-1.
#    - Compute right_sum = sum of elements from index i+1 to end.
#    - If left_sum == right_sum, return i.
# 5. If no equilibrium index is found, return -1.
# 6. Take user input for array size.
# 7. Take user input for array elements.
# 8. Create a Solution object.
# 9. Call equilibrium_index and print result."""

class Solution:
    def equilibrium_index(self, arr: list) -> int:
        n = len(arr)
        for i in range(n):
            left_sum = 0
            right_sum = 0
            for j in range(i):
                left_sum += arr[j]
            for j in range(i+1, n):
                right_sum += arr[j]
            if left_sum == right_sum:
                return i
        return -1
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
sol = Solution()
result = sol.equilibrium_index(arr)
print("Equilibrium index:", result)