""" Maximum Product Subarray
# 1. Define a class Solution.
# 2. Inside it, create a method max_product_subarray that takes an array arr.
# 3. Initialize max_product as arr[0].
# 4. Loop through each subarray starting index i:
#    - Initialize current_product = 1
#    - Loop from index i to end of array j:
#        - current_product *= arr[j]
#        - Update max_product if current_product > max_product
# 5. Return max_product.
# 6. Take user input for array size.
# 7. Take user input for array elements.
# 8. Create a Solution object.
# 9. Call max_product_subarray and print result."""
class Solution:
    def max_product_subarray(self, arr: list) -> int:
        n = len(arr)
        max_product = arr[0]
        for i in range(n):
            current_product = 1
            for j in range(i, n):
                current_product *= arr[j]
                if current_product > max_product:
                    max_product = current_product
        return max_product
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
sol = Solution()
result = sol.max_product_subarray(arr)
print("Maximum product of subarray:", result)