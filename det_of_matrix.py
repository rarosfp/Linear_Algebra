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
R1 = int(input("\nEnter the number of rows: "))
C1 = int(input("\nEnter the number of columns: "))
x1 = (R1,C1)
# For the entries of the first matrix
#
print("\nEnter the entries in a single line (separated by space): ")

mat_1 = list(map(int, input().split()))
  
# For printing the first matrix
#
mat_1 = np.array(mat_1).reshape(R1, C1)
print('\nThe first matrix is: \n\n', mat_1)

# For printing the first matrix dimensions
#
dim_1=mat_1.shape
print('\nThe first matrix dimensios are: \n\n', dim_1)
