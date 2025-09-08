""" Find all symmetric pairs from a pairs of array
# 1. Define a class Solution.
# 2. Inside it, create a method symmetric_pairs that takes an array of pairs (2D list).
# 3. Initialize an empty list result to store symmetric pairs.
# 4. Loop through each pair (a, b) in the array.
# 5. For each pair, loop again through the array to check if there exists a pair (b, a).
# 6. If such a pair exists, add (a, b) to result (only if not already added).
# 7. Return result list of symmetric pairs.
# 8. Take user input for number of pairs.
# 9. Take user input for each pair and store them in a list of lists.
# 10. Create a Solution object.
# 11. Call symmetric_pairs and print result."""

class Solution:
    def symmetric_pairs(self, pairs: list) -> list:
        result = []
        for i in range(len(pairs)):
            a, b = pairs[i]
            for j in range(i+1, len(pairs)):
                if pairs[j][0] == b and pairs[j][1] == a:
                    if (a, b) not in result and (b, a) not in result:
                        result.append((a, b))
        return result
n = int(input("Enter number of pairs: "))
pairs = []
for _ in range(n):
    x, y = map(int, input("Enter pair (two numbers): ").split())
    pairs.append([x, y])
sol = Solution()
result = sol.symmetric_pairs(pairs)
print("Symmetric pairs:", result)