""" Tim Sort (Simplified)
# 1. Define a class Solution.
# 2. Inside it, create a method insertion_sort to sort a small subarray.
# 3. Create a method merge to merge two sorted subarrays.
# 4. Inside tim_sort, divide arr into small chunks (size = 32).
# 5. Sort each chunk using insertion_sort.
# 6. Merge sorted chunks iteratively using merge.
# 7. Return sorted arr.
# 8. Take user input for list of integers.
# 9. Create a Solution object.
# 10. Call tim_sort and print result."""

class Solution:
    def insertion_sort(self, arr: list, left: int, right: int):
        for i in range(left+1, right+1):
            key = arr[i]
            j = i-1
            while j >= left and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key

    def merge(self, arr: list, l: int, m: int, r: int):
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def tim_sort(self, arr: list) -> list:
        n = len(arr)
        RUN = 32
        for i in range(0, n, RUN):
            self.insertion_sort(arr, i, min(i+RUN-1, n-1))
        size = RUN
        while size < n:
            for left in range(0, n, 2*size):
                mid = min(n-1, left+size-1)
                right = min((left + 2*size -1), n-1)
                if mid < right:
                    self.merge(arr, left, mid, right)
            size *= 2
        return arr

arr = list(map(int, input("Enter numbers separated by space: ").split()))
sol = Solution()
result = sol.tim_sort(arr)
print("Sorted array:", result)
