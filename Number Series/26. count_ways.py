""" Count ways to reach the n’th stair
# 1. Define a class Solution.
# 2. Inside it, create a method count_ways that takes n.
# 3. Initialize ways array of size n+1 with all zeros.
# 4. Base cases: ways[0] = 1, ways[1] = 1
# 5. Loop i from 2 to n:
#    - ways[i] = ways[i-1] + ways[i-2]  (step 1 or 2)
# 6. Return ways[n].
# 7. Take user input for n.
# 8. Create a Solution object.
# 9. Call count_ways and print result."""

class Solution:
    def count_ways(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        ways = [0] * (n + 1)
        ways[0], ways[1] = 1, 1
        for i in range(2, n + 1):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[n]

n = int(input("Enter number of stairs: "))
sol = Solution()
result = sol.count_ways(n)
print(f"Number of ways to reach {n}th stair:", result)
