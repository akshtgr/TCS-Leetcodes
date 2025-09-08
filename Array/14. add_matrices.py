""" Program for addition of two matrices
# 1. Define a class Solution.
# 2. Inside it, create a method add_matrices that takes two matrices A and B.
# 3. Initialize result matrix with all 0s of same dimensions as A and B.
# 4. Loop through each row i.
# 5. Inside that, loop through each column j.
#    - result[i][j] = A[i][j] + B[i][j]
# 6. Return the result matrix.
# 7. Take user input for number of rows and columns.
# 8. Take user input for elements of matrix A.
# 9. Take user input for elements of matrix B.
# 10. Create a Solution object.
# 11. Call add_matrices and print result."""

class Solution:
    def add_matrices(self, A: list, B: list) -> list:
        rows = len(A)
        cols = len(A[0])
        result = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                result[i][j] = A[i][j] + B[i][j]
        return result
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("Enter elements of Matrix A row-wise:")
A = []
for _ in range(rows):
    A.append(list(map(int, input().split())))
print("Enter elements of Matrix B row-wise:")
B = []
for _ in range(rows):
    B.append(list(map(int, input().split())))
sol = Solution()
result = sol.add_matrices(A, B)
print("Resultant Matrix after Addition:")
for row in result:
    print(row)