""" Shell Sort
# 1. Define a class Solution.
# 2. Inside it, create a method shell_sort that takes a list arr.
# 3. Initialize gap = len(arr) // 2.
# 4. Loop while gap > 0:
#    - For i from gap to len(arr)-1:
#        - temp = arr[i]
#        - j = i
#        - while j >= gap and arr[j-gap] > temp:
#            - arr[j] = arr[j-gap]
#            - j -= gap
#        - arr[j] = temp
#    - gap //= 2
# 5. Return sorted arr.
# 6. Take user input for list of integers.
# 7. Create a Solution object.
# 8. Call shell_sort and print result."""

class Solution:
    def shell_sort(self, arr: list) -> list:
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j-gap] > temp:
                    arr[j] = arr[j-gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr

arr = list(map(int, input("Enter numbers separated by space: ").split()))
sol = Solution()
result = sol.shell_sort(arr)
print("Sorted array:", result)
