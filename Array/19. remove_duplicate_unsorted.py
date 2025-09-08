""" Remove duplicates from an unsorted array using Map data structure
# 1. Define a class Solution.
# 2. Inside it, create a method remove_duplicates_unsorted that takes an array arr.
# 3. Initialize an empty dictionary seen.
# 4. Initialize an empty list result.
# 5. Loop through each element in arr:
#    - If element not in seen, add it to seen and append it to result.
# 6. Return result list (duplicates removed, first occurrences kept).
# 7. Take user input for array size.
# 8. Take user input for array elements.
# 9. Create a Solution object.
# 10. Call remove_duplicates_unsorted and print result."""

class Solution:
    def remove_duplicates_unsorted(self, arr: list) -> list:
        seen = {}
        result = []
        for num in arr:
            if num not in seen:
                seen[num] = True
                result.append(num)
        return result
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
sol = Solution()
result = sol.remove_duplicates_unsorted(arr)
print("Array after removing duplicates:", result)