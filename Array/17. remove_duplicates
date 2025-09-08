""" Remove duplicates from the sorted array
# 1. Define a class Solution.
# 2. Inside it, create a method remove_duplicates that takes an array arr.
# 3. Initialize a new list result with the first element of arr.
# 4. Loop through arr starting from the second element:
#    - If current element is not equal to the last element in result, append it to result.
# 5. Return the result list.
# 6. Take user input for array size.
# 7. Take user input for sorted array elements.
# 8. Create a Solution object.
# 9. Call remove_duplicates and print result."""

class Solution:
    def remove_duplicates(self, arr: list) -> list:
        if not arr:
            return []
        result = [arr[0]]
        for i in range(1, len(arr)):
            if arr[i] != result[-1]:
                result.append(arr[i])
        return result
n = int(input("Enter size of sorted array: "))
arr = list(map(int, input("Enter sorted array elements: ").split()))
sol = Solution()
result = sol.remove_duplicates(arr)
print("Array after removing duplicates:", result)