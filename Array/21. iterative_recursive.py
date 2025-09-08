""" Average of an array (Iterative and Recursive)
# 1. Define a class Solution.
# 2. Inside it, create two methods: iterative_average and recursive_average.
# 3. iterative_average:
#    - Initialize total = 0.
#    - Loop through each element in arr, add to total.
#    - Return total / n.
# 4. recursive_average:
#    - Base case: if index == n, return 0.
#    - Return (arr[index] + recursive call with index+1) / n after full sum is obtained.
# 5. Take user input for array size.
# 6. Take user input for array elements.
# 7. Create a Solution object.
# 8. Call both methods and print results."""

class Solution:
    def iterative_average(self, arr: list) -> float:
        total = 0
        for num in arr:
            total += num
        return total / len(arr)
    def recursive_average_util(self, arr: list, index: int) -> int:
        if index == len(arr):
            return 0
        return arr[index] + self.recursive_average_util(arr, index + 1)
    def recursive_average(self, arr: list) -> float:
        total = self.recursive_average_util(arr, 0)
        return total / len(arr)
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
sol = Solution()
iter_avg = sol.iterative_average(arr)
rec_avg = sol.recursive_average(arr)
print("Iterative Average:", iter_avg)
print("Recursive Average:", rec_avg)