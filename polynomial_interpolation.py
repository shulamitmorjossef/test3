from colors import bcolors
from matrix_utility import *
from gaussian_elimination import gaussianElimination
from gaussian_elimination import backward_substitution
from gaussian_elimination import forward_substitution


def polynomialInterpolation(table_points, x):
    # matrix1 = [[point[0] ** i for i in range(len(table_points))] for point in table_points] # Makes the initial matrix
    # print(matrix1)
    n = len(table_points)
    matrix = [[0] * (n + 1) for _ in range(n)]
    # matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        x_i = table_points[i][0]
        y_i = table_points[i][1]
        for j in range(n):
            matrix[i][j] = x_i ** j
        matrix[i][-1] = y_i
    print(matrix)
    result = gaussianElimination(matrix)
    if isinstance(result, str):
        print(result)
    else:
        print(bcolors.OKBLUE,"\nSolution for the system:")
        for x1 in result:
            print("{:.6f}".format(x1))
    result2 = sum (result[i] * (x ** i) for i in range(n))
    print('P(X) = '+'+'.join([ '('+str(result[i])+') * x^' + str(i) + ' ' for i in range(len(result))]))
    print(bcolors.OKGREEN, f"\nThe Result of P(X={x}) is:", bcolors.ENDC)
    print(result2)




if __name__ == '__main__':

    table_points = [(0, 0), (1, 0.8415), (2, 0.9093), (3, 0.1411), (4, -0.7568), (5, -0.9589), (6, -0.2794)]
    # table_points = [(1, 3), (2, 4), (3, -1)]

    x = 1
    print(bcolors.OKBLUE, "----------------- Interpolation & Extrapolation Methods -----------------\n", bcolors.ENDC)
    print(bcolors.OKBLUE, "Table Points: ", bcolors.ENDC, table_points)
    print(bcolors.OKBLUE, "Finding an approximation to the point: ", bcolors.ENDC, x,'\n')
    polynomialInterpolation(table_points, x)
    print(bcolors.OKBLUE, "\n---------------------------------------------------------------------------\n", bcolors.ENDC)
