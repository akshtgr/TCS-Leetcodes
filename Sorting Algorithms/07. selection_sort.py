""" Selection Sort
# 1. Define a class Solution.
# 2. Inside it, create a method selection_sort that takes arr.
# 3. Loop i from 0 to n-1:
#    - min_idx = i
#    - Loop j from i+1 to n-1:
#        - If arr[j] < arr[min_idx], min_idx = j
#    - Swap arr[i] and arr[min_idx]
# 4. Return sorted arr.
# 5. Take user input for list of integers.
# 6. Create a Solution object.
# 7. Call selection_sort and print result."""

class Solution:
    def selection_sort(self, arr: list) -> list:
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

arr = list(map(int, input("Enter numbers separated by space: ").split()))
sol = Solution()
result = sol.selection_sort(arr)
print("Sorted array:", result)
