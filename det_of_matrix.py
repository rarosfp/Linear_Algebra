##
##\-\-\-\-\-\-\-\-\-\-\-\ Determinant of matrix calculator -\-\-\-\-\-\-\-\-#
##
##
##\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ By rarosfp \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
##
##
##\-\-\-\-\-\-\-\-\-\-\- in alpha Version (0.1) -\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
#
#
# ---- Import the modules ---- #
#
import numpy as np

# ---- Import the matrix in the program ---- #
#
# For the dimensions of the first matrix
#
print('\nImport the number of Rows and Columns for the first Matrix\n',)
R = int(input("\nEnter the number of rows: "))
C = int(input("\nEnter the number of columns: "))

# For the entries of the first matrix
print("\nEnter the entries in a single line (separated by space): ")

matrix = list(map(int, input().split()))
  
# For the matrix
matrix = np.array(matrix).reshape(R, C)

# Matrix dimensions
dim=matrix.shape

# Displaying the Matrix
print("Numpy Matrix is:\n")
print(matrix)


# calculating the determinant of matrix
det = np.linalg.det(matrix)
  
print("\nDeterminant of given ",dim ," matrix is: \n")
print(int(det))


