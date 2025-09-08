""" Bubble Sort
# 1. Define a class Solution.
# 2. Inside it, create a method bubble_sort that takes arr.
# 3. Loop i from 0 to n-1:
#    - Loop j from 0 to n-i-2:
#        - If arr[j] > arr[j+1], swap arr[j] and arr[j+1]
# 4. Return sorted arr.
# 5. Take user input for list of integers.
# 6. Create a Solution object.
# 7. Call bubble_sort and print result."""

class Solution:
    def bubble_sort(self, arr: list) -> list:
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

arr = list(map(int, input("Enter numbers separated by space: ").split()))
sol = Solution()
result = sol.bubble_sort(arr)
print("Sorted array:", result)
