""" Mean and median of an unsorted array
# 1. Define a class Solution.
# 2. Inside it, create a method mean_and_median that takes an array arr.
# 3. To compute mean:
#    - Sum all elements manually using a loop.
#    - Divide by number of elements.
# 4. To compute median:
#    - Sort the array manually using bubble sort (brute force).
#    - If size is odd, median is middle element.
#    - If size is even, median is average of two middle elements.
# 5. Return mean and median as a tuple.
# 6. Take user input for array size.
# 7. Take user input for array elements.
# 8. Create a Solution object.
# 9. Call mean_and_median and print results."""

class Solution:
    def mean_and_median(self, arr: list) -> tuple:
        n = len(arr)
        # Mean
        total = 0
        for num in arr:
            total += num
        mean = total / n
        # Bubble sort for median
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        # Median
        if n % 2 == 1:
            median = arr[n // 2]
        else:
            median = (arr[(n-1)//2] + arr[n//2]) / 2
        return (mean, median)
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
sol = Solution()
mean, median = sol.mean_and_median(arr)
print("Mean:", mean)
print("Median:", median)