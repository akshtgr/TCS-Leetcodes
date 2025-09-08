""" Counting Rock Samples
# Problem: Given N rock samples with weights, and Q queries with weight ranges [L, R],
# count how many rocks fall into each query range.
#
# Steps:
# 1. Define a class Solution.
# 2. Inside it, create a method count_samples that takes an array rocks and a list of queries.
# 3. For each query [L, R], initialize count = 0.
# 4. Loop through all rocks and check if rock weight is between L and R.
# 5. If yes, increment count.
# 6. Store count in result list.
# 7. Return result list.
# 8. Take user input for number of rocks and their weights.
# 9. Take user input for number of queries.
# 10. For each query, take L and R and store in queries list.
# 11. Create a Solution object.
# 12. Call count_samples and print results."""

class Solution:
    def count_samples(self, rocks: list, queries: list) -> list:
        result = []
        for L, R in queries:
            count = 0
            for weight in rocks:
                if L <= weight <= R:
                    count += 1
            result.append(count)
        return result
n = int(input("Enter number of rocks: "))
rocks = list(map(int, input("Enter rock weights: ").split()))
q = int(input("Enter number of queries: "))
queries = []
for _ in range(q):
    L, R = map(int, input("Enter query range L R: ").split())
    queries.append((L, R))
sol = Solution()
result = sol.count_samples(rocks, queries)
print("Results for each query:", result)