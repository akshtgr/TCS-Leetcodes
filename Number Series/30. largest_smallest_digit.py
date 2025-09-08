""" Largest and smallest digit of a number
# 1. Define a class Solution.
# 2. Inside it, create a method largest_smallest_digit that takes a number n.
# 3. Initialize largest = 0 and smallest = 9.
# 4. Loop while n > 0:
#    - digit = n % 10
#    - If digit > largest, largest = digit
#    - If digit < smallest, smallest = digit
#    - n //= 10
# 5. Return (largest, smallest)
# 6. Take user input for number.
# 7. Create a Solution object.
# 8. Call largest_smallest_digit and print result."""

class Solution:
    def largest_smallest_digit(self, n: int) -> tuple:
        largest = 0
        smallest = 9
        while n > 0:
            digit = n % 10
            if digit > largest:
                largest = digit
            if digit < smallest:
                smallest = digit
            n //= 10
        return (largest, smallest)

num = int(input("Enter a number: "))
sol = Solution()
result = sol.largest_smallest_digit(num)
print(f"Largest digit: {result[0]}, Smallest digit: {result[1]}")
