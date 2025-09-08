""" Sort a K-Increasing-Decreasing Array
# 1. Define a class Solution.
# 2. Inside it, create a method sort_k_inc_dec that takes an array arr.
# 3. Break arr into monotonic subarrays:
#    - Loop through arr and split whenever order changes (inc → dec or dec → inc).
# 4. Collect all subarrays in a list of segments.
# 5. Reverse the decreasing segments to make them sorted in increasing order.
# 6. Merge all sorted subarrays into one sorted array (brute force merge).
# 7. Return the final sorted array.
# 8. Take user input for array size.
# 9. Take user input for array elements.
# 10. Create a Solution object.
# 11. Call sort_k_inc_dec and print result."""

class Solution:
    def sort_k_inc_dec(self, arr: list) -> list:
        n = len(arr)
        segments = []
        start = 0
        increasing = True
        # Step 1: Split into monotonic subarrays
        for i in range(1, n + 1):
            if i == n or (increasing and arr[i] < arr[i - 1]) or (not increasing and arr[i] > arr[i - 1]):
                segment = arr[start:i]
                if not increasing:
                    segment.reverse()
                segments.append(segment)
                start = i
                increasing = not increasing
        # Step 2: Merge all sorted segments (brute force way)
        result = []
        for seg in segments:
            result.extend(seg)
        # Final sort
        for i in range(len(result)):
            for j in range(0, len(result) - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
        return result
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
sol = Solution()
result = sol.sort_k_inc_dec(arr)
print("Sorted array:", result)