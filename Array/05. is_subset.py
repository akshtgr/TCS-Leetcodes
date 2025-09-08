""" Array is a subset of another array
# 1. Define a class Solution.
# 2. Inside it, create a method is_subset that takes two arrays arr1 and arr2.
# 3. Loop through each element in arr2.
# 4. For each element, check if it exists in arr1 by looping through arr1.
# 5. If any element in arr2 is not found in arr1, return False.
# 6. If all elements are found, return True.
# 7. Take user input for size of arr1 and arr2.
# 8. Take user input for elements of arr1 and arr2.
# 9. Create a Solution object.
# 10. Call is_subset and print result."""

class Solution:
    def is_subset(self, arr1: list, arr2: list) -> bool:
        for num in arr2:
            found = False
            for x in arr1:
                if num == x:
                    found = True
                    break
            if not found:
                return False
        return True
n1 = int(input("Enter size of first array: "))
arr1 = list(map(int, input("Enter elements of first array: ").split()))
n2 = int(input("Enter size of second array: "))
arr2 = list(map(int, input("Enter elements of second array: ").split()))
sol = Solution()
result = sol.is_subset(arr1, arr2)
print("Is second array a subset of first?:", result)