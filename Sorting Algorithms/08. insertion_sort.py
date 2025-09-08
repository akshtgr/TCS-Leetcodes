""" Insertion Sort
# 1. Define a class Solution.
# 2. Inside it, create a method insertion_sort that takes arr.
# 3. Loop i from 1 to n-1:
#    - key = arr[i]
#    - j = i-1
#    - while j >= 0 and arr[j] > key:
#        - arr[j+1] = arr[j]
#        - j -= 1
#    - arr[j+1] = key
# 4. Return sorted arr.
# 5. Take user input for list of integers.
# 6. Create a Solution object.
# 7. Call insertion_sort and print result."""

class Solution:
    def insertion_sort(self, arr: list) -> list:
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i-1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

arr = list(map(int, input("Enter numbers separated by space: ").split()))
sol = Solution()
result = sol.insertion_sort(arr)
print("Sorted array:", result)
