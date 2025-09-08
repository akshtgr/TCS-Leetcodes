""" Largest element in an array
# 1. Define a class Solution.
# 2. Inside it, create a method largest that takes an array arr.
# 3. Initialize largest as the first element of arr.
# 4. Loop through each element in arr:
#    - If current element > largest, update largest.
# 5. After loop ends, return largest element.
# 6. Take user input for array size.
# 7. Take user input for array elements.
# 8. Create a Solution object.
# 9. Call largest and print result."""

class Solution:
    def largest(self, arr: list) -> int:
        largest = arr[0]
        for num in arr:
            if num > largest:
                largest = num
        return largest
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
sol = Solution()
result = sol.largest(arr)
print("Largest element in array:", result)