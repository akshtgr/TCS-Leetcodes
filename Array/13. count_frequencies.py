""" Counting frequencies of array elements
# 1. Define a class Solution.
# 2. Inside it, create a method count_frequencies that takes an array arr.
# 3. Initialize an empty dictionary freq to store element → count mapping.
# 4. Loop through each element in arr:
#    - If element already in freq, increment its count by 1.
#    - Otherwise, set its count to 1.
# 5. Return the freq dictionary.
# 6. Take user input for array size.
# 7. Take user input for array elements.
# 8. Create a Solution object.
# 9. Call count_frequencies and print result."""

class Solution:
    def count_frequencies(self, arr: list) -> dict:
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        return freq
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
sol = Solution()
result = sol.count_frequencies(arr)
print("Frequencies of array elements:", result)