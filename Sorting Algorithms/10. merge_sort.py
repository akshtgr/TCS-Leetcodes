""" Merge Sort
# 1. Define a class Solution.
# 2. Inside it, create a method merge_sort that takes arr.
# 3. If len(arr) > 1:
#    - Find mid = len(arr)//2
#    - Divide arr into left = arr[:mid], right = arr[mid:]
#    - Recursively call merge_sort on left and right
#    - Merge left and right into arr
# 4. Return sorted arr.
# 5. Take user input for list of integers.
# 6. Create a Solution object.
# 7. Call merge_sort and print result."""

class Solution:
    def merge_sort(self, arr: list) -> list:
        if len(arr) > 1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            self.merge_sort(left)
            self.merge_sort(right)
            i = j = k = 0
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
        return arr

arr = list(map(int, input("Enter numbers separated by space: ").split()))
sol = Solution()
result = sol.merge_sort(arr)
print("Sorted array:", result)
