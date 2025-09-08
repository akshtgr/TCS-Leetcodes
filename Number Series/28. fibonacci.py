""" Fibonacci numbers
# 1. Define a class Solution.
# 2. Inside it, create a method fibonacci that takes n (number of terms).
# 3. Initialize a list fib with first two terms [0, 1] (if n >= 2).
# 4. Loop i from 2 to n-1:
#    - fib.append(fib[i-1] + fib[i-2])
# 5. Handle cases when n = 1 separately.
# 6. Return fib list up to n terms.
# 7. Take user input for n.
# 8. Create a Solution object.
# 9. Call fibonacci and print result."""

class Solution:
    def fibonacci(self, n: int) -> list:
        if n == 0:
            return []
        if n == 1:
            return [0]
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib

n = int(input("Enter number of Fibonacci terms: "))
sol = Solution()
result = sol.fibonacci(n)
print("Fibonacci series:", result)
