""" Radix Sort
# 1. Define a class Solution.
# 2. Inside it, create a method radix_sort that takes a list arr.
# 3. Find max_num = max(arr) to know number of digits.
# 4. Initialize exp = 1.
# 5. Loop while max_num // exp > 0:
#    - Perform counting sort based on digit at exp place.
#    - Increment exp *= 10
# 6. Return sorted arr.
# 7. Take user input for list of integers.
# 8. Create a Solution object.
# 9. Call radix_sort and print result."""

class Solution:
    def counting_sort_exp(self, arr: list, exp: int) -> list:
        n = len(arr)
        output = [0]*n
        count = [0]*10
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1
        for i in range(1,10):
            count[i] += count[i-1]
        i = n-1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10]-1] = arr[i]
            count[index % 10] -= 1
            i -= 1
        for i in range(n):
            arr[i] = output[i]
        return arr

    def radix_sort(self, arr: list) -> list:
        if len(arr) == 0:
            return arr
        max_num = max(arr)
        exp = 1
        while max_num // exp > 0:
            self.counting_sort_exp(arr, exp)
            exp *= 10
        return arr

arr = list(map(int, input("Enter numbers separated by space: ").split()))
sol = Solution()
result = sol.radix_sort(arr)
print("Sorted array:", result)
