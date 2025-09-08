""" Sort elements by frequency
# 1. Define a class Solution.
# 2. Inside it, create a method sort_by_frequency that takes an array arr.
# 3. Initialize a dictionary freq to count frequency of each element.
# 4. Loop through arr to populate freq dictionary.
# 5. Convert dictionary items to a list of tuples (element, frequency).
# 6. Sort this list manually:
#    - First by decreasing frequency
#    - If frequencies are equal, sort by increasing element value
# 7. Initialize result list and expand each element according to its frequency.
# 8. Return the result list.
# 9. Take user input for array size.
# 10. Take user input for array elements.
# 11. Create a Solution object.
# 12. Call sort_by_frequency and print result."""

class Solution:
    def sort_by_frequency(self, arr: list) -> list:
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        freq_list = list(freq.items())
        # Manual sort: decreasing frequency, then increasing element
        for i in range(len(freq_list)):
            for j in range(0, len(freq_list)-i-1):
                if (freq_list[j][1] < freq_list[j+1][1]) or (freq_list[j][1] == freq_list[j+1][1] and freq_list[j][0] > freq_list[j+1][0]):
                    freq_list[j], freq_list[j+1] = freq_list[j+1], freq_list[j]
        result = []
        for num, count in freq_list:
            result.extend([num]*count)
        return result
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
sol = Solution()
result = sol.sort_by_frequency(arr)
print("Array sorted by frequency:", result)