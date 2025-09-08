""" Quick Sort
# 1. Define a class Solution.
# 2. Inside it, create a method quick_sort that takes arr, low, high.
# 3. Create a helper method partition:
#    - Choose last element as pivot.
#    - Initialize i = low - 1
#    - Loop j from low to high-1:
#        - If arr[j] <= pivot, increment i, swap arr[i] and arr[j]
#    - Swap arr[i+1] and pivot
#    - Return i+1
# 4. In quick_sort, recursively sort left and right partitions.
# 5. Return sorted arr.
# 6. Take user input for list of integers.
# 7. Create a Solution object.
# 8. Call quick_sort and print result."""

class Solution:
    def partition(self, arr: list, low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

    def quick_sort(self, arr: list, low: int, high: int) -> list:
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi-1)
            self.quick_sort(arr, pi+1, high)
        return arr

arr = list(map(int, input("Enter numbers separated by space: ").split()))
sol = Solution()
result = sol.quick_sort(arr, 0, len(arr)-1)
print("Sorted array:", result)
