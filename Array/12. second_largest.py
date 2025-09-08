""" Second largest element in an array
# 1. Define a class Solution.
# 2. Inside it, create a method second_largest that takes an array arr.
# 3. Initialize largest and second_largest as negative infinity (very small number).
# 4. Loop through each element in arr:
#    - If current element > largest:
#         second_largest = largest
#         largest = current element
#    - Else if current element > second_largest and not equal to largest:
#         second_largest = current element
# 5. If second_largest is still negative infinity, return -1 (no second largest exists).
# 6. Otherwise, return second_largest.
# 7. Take user input for array size.
# 8. Take user input for array elements.
# 9. Create a Solution object.
# 10. Call second_largest and print result."""

class Solution:
    def second_largest(self, arr: list) -> int:
        largest = float('-inf')
        second_largest = float('-inf')
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
        if second_largest == float('-inf'):
            return -1
        return second_largest
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
sol = Solution()
result = sol.second_largest(arr)
print("Second largest element in array:", result)