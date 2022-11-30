##
##\-\-\-\-\-\-\-\-\-\-\-\ Matrix Multiplication with number -\-\-\-\-\-\-\-\-\-\-\-\-\-#
##
##
##\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ By rarosfp \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
##
##
##\-\-\-\-\-\-\-\-\-\-\-\- In beta Version (b-01) -\-\-\-\-\-\-\-\-\-\-\-\-\-#
#
#
# ---- Import the modules ---- #
#
import numpy as np

# ---- Import the matrix in the program ---- #
#
# For the dimensions of the matrix
#
print('\nImport the number of Rows and Columns for the Matrix\n',)
R1 = int(input("\nEnter the number of rows: "))
C1 = int(input("\nEnter the number of columns: "))
x1 = (R1, C1)
num_in_mat1= R1 * C1 # calculate the elements in the matrix

# For the entries of the first matrix
#
print("\nEnter the entries in a single line (separated by space): ")

mat_1 = list(map(int, input().split()))
i = len(mat_1)

while num_in_mat1 != i :
    # For the entries of the first matrix
    print("\nThe Matrix with dimensions ",(R1, C1)," need ", num_in_mat1 ," of entries! \n\nEnter ",num_in_mat1 ," entries again in a single line (separated by space): ")
    mat_1 = list(map(int, input().split()))
    i = len(mat_1)
# For printing the first matrix
#
mat_1 = np.array(mat_1).reshape(R1, C1)
print('\nThe first matrix is: \n\n', mat_1)

# For printing the first matrix dimensions
#
dim_1=mat_1.shape
print('\nThe first matrix dimensios are: \n\n', dim_1)


# ---- Import the number of multiplication in the program ---- #
#
print('\nImport the number of multiplication in the program. \n',)
N = int(input("\nEnter the number: "))

# For multiply the matrix with the number
