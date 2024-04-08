import numpy as np
import matrix_utility as mt
from colors import bcolors
from matrix_utility import swap_rows_elementary_matrix, row_addition_elementary_matrix


def lu(A):
        N = len(A)
        L = np.eye(N) # Create an identity matrix of size N x N

        for i in range(N):
    
            # Partial Pivoting: Find the pivot row with the largest absolute value in the current column
            pivot_row = i
            v_max = A[pivot_row][i]
            for j in range(i + 1, N):
                if abs(A[j][i]) > v_max:
                    v_max = A[j][i]
                    pivot_row = j

            # if a principal diagonal element is zero,it denotes that matrix is singular,
            # and will lead to a division-by-zero later.
            if A[i][pivot_row] == 0:
                raise ValueError("can't perform LU Decomposition")

            # Swap the current row with the pivot row
            if pivot_row != i:
                e_matrix = swap_rows_elementary_matrix(N, i, pivot_row)
                print(f"elementary matrix for swap between row {i} to row {pivot_row} :\n {e_matrix} \n")
                A = np.dot(e_matrix, A)
                print(f"The matrix after elementary operation :\n {A}")
                print(bcolors.OKGREEN,"---------------------------------------------------------------------------", bcolors.ENDC)

            for j in range(i + 1, N):
    
                #  Compute the multiplier
                m = -A[j][i] / A[i][i]
                e_matrix = row_addition_elementary_matrix(N, j, i, m)
                e_inverse = np.linalg.inv(e_matrix)
                L = np.dot(L, e_inverse)
                A = np.dot(e_matrix, A)
                print(f"elementary matrix to zero the element in row {j} below the pivot in column {i} :\n {e_matrix} \n")
                print(f"The matrix after elementary operation :\n {A}")
                print(bcolors.OKGREEN,"---------------------------------------------------------------------------", bcolors.ENDC)

        U = A
        return L, U


# function to calculate the values of the unknowns
def backward_substitution(mat):
    N = len(mat)
    x = np.zeros(N)  # An array to store solution

    # Start calculating from last equation up to the first
    for i in range(N - 1, -1, -1):

        x[i] = mat[i][N]

        # Initialize j to i+1 since matrix is upper triangular
        for j in range(i + 1, N):
            x[i] -= mat[i][j] * x[j]

        x[i] = (x[i] / mat[i][i])

    return x

def lu_solve(A_b):
    L, U = lu(A_b)
    print("Lower triangular matrix L:\n", L)
    print("Upper triangular matrix U:\n", U)

    result = backward_substitution(U)
    print(bcolors.OKBLUE,"\nSolution for the system:")
    for x in result:
        print("{:.6f}".format(x))


def gauss_seidel_formula(matrix, Xr, b):
    _L = mt.l_mat(matrix) # calculate the L matrix
    _D = mt.diagonal_mat(matrix) # calculate the D matrix
    _U = mt.U_mat(matrix) # calculate the U matrix

    sum_L_D = mt.sum_matrices(_L, _D) # calculate: (L+D)
    inverse_sum_L_D = mt.inverse(sum_L_D) # calculate: (L+D)^-1
    inverse_mult_U = mt.matrix_multiply(inverse_sum_L_D, _U) # calculate: (L+D)^-1 * U
    becomes_minus = mt.mult_matrix_in_scalar(inverse_mult_U, -1) # calculate: -(L+D)^-1 * U
    mat_mult_x0 = mt.MulMatrixVector(becomes_minus, Xr) # calculate: (-(L+D)^-1 * U) *X0

    inverse_mult_b = mt.MulMatrixVector(inverse_sum_L_D, b) # calculate: (L+D)^-1 * b

    result_vector = mt.sum_vectors(mat_mult_x0, inverse_mult_b)
    return result_vector

# becomes_minus , זה הG של נוסחת זיידל

# כדי למצוא את הg המדובר צריך לשלוח את becomes_minus לפונקציית הנורמה



if __name__ == '__main__':


    A_b = [[1, -1, 2, -1, -8],
        [2, -2, 3, -3, -20],
        [1, 1, 1, 0, -2],
        [1, -1, 4, 3, 4]]


    lu_solve(A_b)