""" Counting Sort
# 1. Define a class Solution.
# 2. Inside it, create a method counting_sort that takes arr.
# 3. Find max_val = max(arr)
# 4. Initialize count array of size max_val+1 with zeros.
# 5. Count occurrences of each element in arr.
# 6. Construct sorted array by looping through count array.
# 7. Return sorted array.
# 8. Take user input for list of integers.
# 9. Create a Solution object.
# 10. Call counting_sort and print result."""

class Solution:
    def counting_sort(self, arr: list) -> list:
        if len(arr) == 0:
            return arr
        max_val = max(arr)
        count = [0]*(max_val+1)
        for num in arr:
            count[num] += 1
        sorted_arr = []
        for i in range(len(count)):
            sorted_arr.extend([i]*count[i])
        return sorted_arr

arr = list(map(int, input("Enter numbers separated by space: ").split()))
sol = Solution()
result = sol.counting_sort(arr)
print("Sorted array:", result)
