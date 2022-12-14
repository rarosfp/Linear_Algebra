##
##\-\-\-\-\-\-\-\-\-\-\-\ Matrices Multiplication -\-\-\-\-\-\-\-\-\-\-\-\-\-#
##
##
##\-\-\-\-\-\-\-\-\-\-\-\-\-\-\ By rarosfp \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-#
##
##
##\-\-\-\-\-\-\-\-\-\-\-\- In beta Version (v-03) -\-\-\-\-\-\-\-\-\-\-\-\-\-#
#
#
# ---- Import the modules ---- #
#
import numpy as np

# ---- Import the matrices in the program ---- #
#
# For the dimensions of the first matrix
#
print('\nImport the number of Rows and Columns for the first Matrix\n',)
R1 = int(input("\nEnter the number of rows: "))
C1 = int(input("\nEnter the number of columns: "))
x1 = (R1, C1)
num_in_mat1= R1 * C1 # calculate the elements in the first matrix

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

# For the dimensions of the Second matrix
#
print('\nImport the number of Rows and Columns for the Second Matrix\n')
R2 = int(input("\nEnter the number of rows: "))
C2 = int(input("\nEnter the number of columns: "))
x2=(R2, C2)
num_in_mat2= R2 * C2 # calculate the elements in the second matrix

#For the entries of the Second matrix
#
#The if statement investigates the dimensions of the second matrix.
#If the dimension is equal to the dimension of the first matrix,
#Then reshape the second matrix,
#Otherwise, continue.

if x1 == x2:
    
    print("\nEnter the entries in a single line (separated by space): ")
    mat_2 = list(map(int, input().split()))
    i = len(mat_2)
    
    while num_in_mat2 != i :
        print("\nThe Matrix with dimensions ",(R2, C2)," need ", num_in_mat2 ," of entries! \n\nEnter ",num_in_mat2 ," entries again in a single line (separated by space): ")
        mat_2 = list(map(int, input().split()))
        i = len(mat_2)
    # For printing the second matrix
    #
    mat_2 = np.array(mat_2).reshape(C2, R2)
    print('\nThe Second matrix is: \n', mat_2)
    # For printing the first matrix dimensions
    #
    dim_2=mat_2.shape
    print('\nThe Second matrix dimensios are: \n', dim_2)
    
elif C1 == R2:
    print("\nEnter the entries in a single line (separated by space): ")
    mat_2 = list(map(int, input().split()))
    i = len(mat_2)
    
    while num_in_mat2 != i :
        print("\nThe Matrix with dimensions ",(R2, C2)," need ", num_in_mat2 ," of entries! \n\nEnter ",num_in_mat2 ," entries again in a single line (separated by space): ")
        mat_2 = list(map(int, input().split()))
        i = len(mat_2)
    # For printing the second matrix
    #
    mat_2 = np.array(mat_2).reshape(R2, C2)
    print('\nThe Second matrix is: \n', mat_2)
    # For printing the first matrix dimensions
    #
    dim_2=mat_2.shape
    print('\nThe Second matrix dimensios are: \n', dim_2)

elif C1 == C2:
    print("\nEnter the entries in a single line (separated by space): ")
    mat_2 = list(map(int, input().split()))
    i = len(mat_2)
    
    while num_in_mat2 != i :
        print("\nThe Matrix with dimensions ",(R2, C2)," need ", num_in_mat2 ," of entries! \n\nEnter ",num_in_mat2 ," entries again in a single line (separated by space): ")
        mat_2 = list(map(int, input().split()))
        i = len(mat_2)
    # For printing the second matrix
    #
    mat_2 = np.array(mat_2).reshape(C2, R2)
    print('\nThe Second matrix is: \n', mat_2)
    # For printing the first matrix dimensions
    #
    dim_2=mat_2.shape
    print('\nThe Second matrix dimensios are: \n', dim_2)
    
else:
    print('\nCalculation error!\n\nIn matrix multiplication, the columns of Matrix A must equal the rows of Matrix B. (x*z)(z*y)=(x*y)')
    print('\n\nImport again the number of Rows and Columns for the new Matrix\n')
    R2 = int(input("\nEnter the number of rows: "))
    C2 = int(input("\nEnter the number of columns: "))
    x2=(R2, C2)
    num_in_mat2= R2 * C2
    
    if x1 == x2:
        print("\nEnter the entries in a single line (separated by space): ")
        mat_2 = list(map(int, input().split()))
        i = len(mat_2)
    
        while num_in_mat2 != i :
            print("\nThe Matrix with dimensions ",(R2, C2)," need ", num_in_mat2 ," of entries! \n\nEnter ",num_in_mat2 ," entries again in a single line (separated by space): ")
            mat_2 = list(map(int, input().split()))
            i = len(mat_2)
        # For printing the second matrix
        #
        mat_2 = np.array(mat_2).reshape(C2, R2)
        print('\nThe Second matrix is: \n', mat_2)
        # For printing the first matrix dimensions
        #
        dim_2=mat_2.shape
        print('\nThe Second matrix dimensios are: \n', dim_2)
    
    elif C1 == R2:
        print("\nEnter the entries in a single line (separated by space): ")
        mat_2 = list(map(int, input().split()))
        i = len(mat_2)
    
        while num_in_mat2 != i :
            print("\nThe Matrix with dimensions ",(R2, C2)," need ", num_in_mat2 ," of entries! \n\nEnter ",num_in_mat2 ," entries again in a single line (separated by space): ")
            mat_2 = list(map(int, input().split()))
            i = len(mat_2)
        # For printing the second matrix
        #
        mat_2 = np.array(mat_2).reshape(R2, C2)
        print('\nThe Second matrix is: \n', mat_2)
        # For printing the first matrix dimensions
        #
        dim_2=mat_2.shape
        print('\nThe Second matrix dimensios are: \n', dim_2)
    elif C1 == C2:
        print("\nEnter the entries in a single line (separated by space): ")
        mat_2 = list(map(int, input().split()))
        i = len(mat_2)
    
        while num_in_mat2 != i :
            print("\nThe Matrix with dimensions ",(R2, C2)," need ", num_in_mat2 ," of entries! \n\nEnter ",num_in_mat2 ," entries again in a single line (separated by space): ")
            mat_2 = list(map(int, input().split()))
            i = len(mat_2)
        # For printing the second matrix
        #
        mat_2 = np.array(mat_2).reshape(C2, R2)
        print('\nThe Second matrix is: \n', mat_2)
        # For printing the first matrix dimensions
        #
        dim_2=mat_2.shape
        print('\nThe Second matrix dimensios are: \n', dim_2)

# ---- Multiply the matricies ---- #

# define the function of matrix multiplication
#
def mat_multiplication(matrix1,matrix2):
    try:
        result=np.matmul(matrix1, matrix2)
        message="Multiplication of matrices completed!"
        dim=result.shape
    except:
        raise Exception('An error occured. Cannot multiply matrices.')
    return message, result, dim

# call the function of matmultiply
#
message, result, dim=mat_multiplication(mat_1,mat_2)

# call the function of matmultiply
#
print('\n',message)
print("\nThe resultant matrix is:\n\n",result)
print("\nThe dimensions of the resultant matrix are:\n\n",dim)
input()

