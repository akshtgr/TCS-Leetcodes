""" Non-Repeating Element
# 1. Define a class Solution.
# 2. Inside it, create a method non_repeating that takes an array arr and returns the first non-repeating element.
# 3. Initialize an empty dictionary freq to count occurrences of each element.
# 4. Loop through arr and count frequency of each element.
# 5. Loop again through arr in original order:
#    - If the frequency of an element is 1, return that element immediately.
# 6. If no non-repeating element is found, return -1.
# 7. Take user input for array size.
# 8. Take user input for array elements.
# 9. Create a Solution object.
# 10. Call non_repeating with the array and print result."""

class Solution:
    def non_repeating(self, arr: list) -> int:
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for num in arr:
            if freq[num] == 1:
                return num
        return -1
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
sol = Solution()
result = sol.non_repeating(arr)
print("First non-repeating element:", result)