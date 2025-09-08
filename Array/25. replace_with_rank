""" Replace each element of the Array with its corresponding rank
# 1. Define a class Solution.
# 2. Inside it, create a method replace_with_rank that takes an array arr.
# 3. Copy arr and sort it manually using bubble sort to get sorted_arr.
# 4. Initialize a dictionary rank_map to store element → rank.
# 5. Loop through sorted_arr and assign ranks starting from 1 (skip duplicates).
# 6. Loop through original arr and replace each element with its rank from rank_map.
# 7. Return the new array with ranks.
# 8. Take user input for array size.
# 9. Take user input for array elements.
# 10. Create a Solution object.
# 11. Call replace_with_rank and print result."""

class Solution:
    def replace_with_rank(self, arr: list) -> list:
        n = len(arr)
        sorted_arr = arr.copy()
        # Bubble sort
        for i in range(n):
            for j in range(0, n-i-1):
                if sorted_arr[j] > sorted_arr[j+1]:
                    sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
        rank_map = {}
        rank = 1
        for num in sorted_arr:
            if num not in rank_map:
                rank_map[num] = rank
                rank += 1
        result = [rank_map[num] for num in arr]
        return result
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
sol = Solution()
result = sol.replace_with_rank(arr)
print("Array with ranks:", result)