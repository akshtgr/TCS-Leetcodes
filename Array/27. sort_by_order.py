""" Sort an array according to the order defined by another array
# 1. Define a class Solution.
# 2. Inside it, create a method sort_by_order that takes two arrays: arr1 and arr2.
# 3. Initialize an empty result list.
# 4. Loop through each element in arr2:
#    - Loop through arr1 and append all occurrences of current element from arr2 to result.
# 5. After processing arr2, loop through arr1:
#    - Append elements not in arr2 to result in original order.
# 6. Return the result list.
# 7. Take user input for size of arr1 and arr2.
# 8. Take user input for elements of arr1 and arr2.
# 9. Create a Solution object.
# 10. Call sort_by_order and print result."""

class Solution:
    def sort_by_order(self, arr1: list, arr2: list) -> list:
        result = []
        used = [False] * len(arr1)
        # Add elements according to arr2
        for num in arr2:
            for i in range(len(arr1)):
                if arr1[i] == num and not used[i]:
                    result.append(arr1[i])
                    used[i] = True
        # Add remaining elements not in arr2
        for i in range(len(arr1)):
            if not used[i]:
                result.append(arr1[i])
        return result
n1 = int(input("Enter size of first array: "))
arr1 = list(map(int, input("Enter elements of first array: ").split()))
n2 = int(input("Enter size of second array: "))
arr2 = list(map(int, input("Enter elements of second array: ").split()))
sol = Solution()
result = sol.sort_by_order(arr1, arr2)
print("Array sorted according to second array:", result)