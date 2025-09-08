""" Bucket Sort
# 1. Define a class Solution.
# 2. Inside it, create a method bucket_sort that takes a list arr.
# 3. Find max_value = max(arr).
# 4. Initialize buckets = [[] for _ in range(max_value+1)].
# 5. Place each element arr[i] in corresponding bucket[arr[i]].
# 6. Flatten the buckets into a sorted list.
# 7. Return sorted list.
# 8. Take user input for list of integers.
# 9. Create a Solution object.
# 10. Call bucket_sort and print result."""

class Solution:
    def bucket_sort(self, arr: list) -> list:
        if len(arr) == 0:
            return arr
        max_value = max(arr)
        buckets = [[] for _ in range(max_value+1)]
        for num in arr:
            buckets[num].append(num)
        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(bucket)
        return sorted_arr

arr = list(map(int, input("Enter numbers separated by space: ").split()))
sol = Solution()
result = sol.bucket_sort(arr)
print("Sorted array:", result)
