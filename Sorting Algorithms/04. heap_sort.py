""" Heap Sort
# 1. Define a class Solution.
# 2. Inside it, create a method heapify that maintains max-heap.
# 3. Inside it, create a method heap_sort that takes arr.
# 4. Build max heap for arr.
# 5. Swap root with last element and reduce heap size.
# 6. Call heapify for root.
# 7. Repeat until heap size > 1.
# 8. Return sorted arr.
# 9. Take user input for list of integers.
# 10. Create a Solution object.
# 11. Call heap_sort and print result."""

class Solution:
    def heapify(self, arr: list, n: int, i: int):
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heap_sort(self, arr: list) -> list:
        n = len(arr)
        for i in range(n//2-1, -1, -1):
            self.heapify(arr, n, i)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
        return arr

arr = list(map(int, input("Enter numbers separated by space: ").split()))
sol = Solution()
result = sol.heap_sort(arr)
print("Sorted array:", result)
