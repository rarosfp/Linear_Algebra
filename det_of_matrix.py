##
##\-\-\-\-\-\-\-\-\-\-\ Determinant of matrix calculator \-\-\-\-\-\-\-\-\-\-#
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
# For the dimensions of the Matrix
#

print('\nImport the number of Rows and Columns for the first Matrix\n',)
R = int(input("\nEnter the number of rows: "))
C = int(input("\nEnter the number of columns: "))
num_in_mat= R * C # calculate the elements in the matrix 

while R != C :

    print('\nThe Matrix Determinant can only be calculated in a square matrix!\n\nImport again the number of Rows and Columns for the Matrix\n',)
    R = int(input("\nEnter the number of rows: "))
    C = int(input("\nEnter the number of columns: "))


# For the entries of the first matrix
print("\nEnter the entries in a single line (separated by space): ")
matrix = list(map(int, input().split()))

i = 1 # counter for the next while

while num_in_mat != i :
    # For the entries of the first matrix
    print("\nThe Matrix with dimensions ",(R, C)," need ", num_in_mat ," of entries! \n\nEnter ",num_in_mat ," entries again in a single line (separated by space): ")
    matrix = list(map(int, input().split()))
    i = len(matrix)
    
# The matrix
matrix = np.array(matrix).reshape(R, C)

# The dimensions of the matrix
dim=matrix.shape

# Displaying the Matrix
print("\nThe Matrix is:\n")
print(matrix)

# calculating and displaying the determinant of matrix
det = np.linalg.det(matrix)
print("\nDeterminant of given ",dim ," matrix is: \n")
print(int(det))


