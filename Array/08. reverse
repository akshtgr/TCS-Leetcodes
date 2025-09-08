""" Reverse an array or string
# 1. Define a class Solution.
# 2. Inside it, create a method reverse that takes arr (which can be a list of numbers or a string).
# 3. If arr is a string, convert it to a list of characters for processing.
# 4. Initialize an empty list reversed_arr.
# 5. Loop backwards from the last index to the first index of arr.
# 6. Append each element to reversed_arr.
# 7. If input was a string, join reversed_arr into a string before returning.
# 8. Otherwise, return reversed_arr as a list.
# 9. Take user input for type choice (array or string).
# 10. Take input accordingly and process.
# 11. Create a Solution object.
# 12. Call reverse and print result."""

class Solution:
    def reverse(self, arr):
        is_string = False
        if isinstance(arr, str):
            arr = list(arr)
            is_string = True
        reversed_arr = []
        for i in range(len(arr)-1, -1, -1):
            reversed_arr.append(arr[i])
        if is_string:
            return "".join(reversed_arr)
        return reversed_arr
choice = input("Do you want to reverse an array or string? (array/string): ")
sol = Solution()
if choice == "array":
    n = int(input("Enter size of array: "))
    arr = list(map(int, input("Enter array elements: ").split()))
    result = sol.reverse(arr)
    print("Reversed array:", result)
else:
    s = input("Enter a string: ")
    result = sol.reverse(s)
    print("Reversed string:", result)