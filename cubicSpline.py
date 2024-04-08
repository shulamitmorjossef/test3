import jacobi_utilities
from sympy import *
from gaussian_elimination import gaussianElimination
from colors import bcolors
from gaussian_elimination import backward_substitution
from gaussian_elimination import forward_substitution
x = Symbol('x')
import numpy as np


# def check_point(f, n, x0, s_list):
#     if(x0 < f[0][0]):
#         print(
#             "\nx0 smaller than f(x" + str(0) + ") = " + str(f[0][0]) + " so:")
#         print("s" + str(0) + "(" + str(x0) + ") = " + str(float(s_list[0].subs(x, x0))))
#     else:
#         if(x0 > f[n-1][0]):
#             print(
#                 "\nx0 bigger than f(x" + str(n) + ") = " + str(f[n-1][0]) + " so:")
#             print("s" + str(n-1) + "(" + str(x0) + ") = " + str(float(s_list[n-2].subs(x, x0))))
#
#         else:
#             for i in range(n-1):
#                 if(x0 > f[i][0] and x0 < f[i+1][0]):
#                     print(
#                         "\nx0 between f(x" + str(i+1) + ") = " + str(f[i][0]) + " and f(x" + str(i+2) + ") = " + str(
#                             f[i+1][0]) + " so:")
#                     print("s" + str(i+1) + "(" + str(x0) + ") = " + str(float(s_list[i].subs(x, x0))))


def build_s_printx0(f, x0, n, result):
    s_list = [None] * n
    for i in range(n-1):
        h_i = f[i+1][0] - f[i][0]
        s_list[i] = ((f[i+1][1] * (x - f[i][0]))/h_i - (f[i][1] * (x - f[i+1][0])) / h_i
                    + result[i+1] / 6 * (((x - f[i][0]) ** 3)/h_i - h_i * (x - f[i][0]))
                   - result[i] / 6 * (((x - f[i+1][0]) ** 3)/h_i - h_i * (x - f[i+1][0])))
        print("s" + str(i) + "(x) = " + str(s_list[i]))

    if (x0 < f[0][0]):
        print(
            "\nx0 smaller than f(x" + str(0) + ") = " + str(f[0][0]) + " so:")
        print("s" + str(0) + "(" + str(x0) + ") = " + str(float(s_list[0].subs(x, x0))))
    else:
        if (x0 > f[n - 1][0]):
            print(
                "\nx0 bigger than f(x" + str(n) + ") = " + str(f[n - 1][0]) + " so:")
            print("s" + str(n - 1) + "(" + str(x0) + ") = " + str(float(s_list[n - 2].subs(x, x0))))

        else:
            for i in range(n - 1):
                if (x0 > f[i][0] and x0 < f[i + 1][0]):
                    print(
                        "\nx0 between f(x" + str(i + 1) + ") = " + str(f[i][0]) + " and f(x" + str(
                            i + 2) + ") = " + str(
                            f[i + 1][0]) + " so:")
                    print("s" + str(i + 1) + "(" + str(x0) + ") = " + str(float(s_list[i].subs(x, x0))))


def natural_cubic_spline(f, x0):
    n = len(f)
    matrix = [[0] * (n + 1) for _ in range(n)]
    matrix[0][0] = 1
    matrix[n-1][n-1] = 1



    for i in range(1, n-1):
        h0 = f[i][0] - f[i-1][0]
        h1 = f[i+1][0] - f[i][0]
        for j in range(0,n):
            if(i == j):
                matrix[i][j] = 1/3 * (h0 + h1)
                matrix[i][j-1] = 1/6 * h0
                matrix[i][j+1] = 1/6 * h1
        matrix[i][n] = (f[i+1][1] - f[i][1])/h1 - (f[i][1] - f[i-1][1])/h0

    print(np.array(matrix))
    result = gaussianElimination(matrix)
    if isinstance(result, str):
        print(result)
    else:
        print(bcolors.OKBLUE, "\nSolution for the system:")
        for x1 in result:
            print("{:.6f}".format(x1))


    build_s_printx0(f, x0, n, result)
def cubic_spline(f, x0, Fx_0, Fx_n):

    n = len(f)
    matrix = [[0] * (n + 1) for _ in range(n)]


    h0 = f[1][0] - f[0][0]
    h_n_1 = f[n - 1][0] - f[n - 2][0]

    matrix[0][0] = h0 / 3
    matrix[0][1] = h0 / 6
    matrix[n - 1][n - 1] = h_n_1 / 3
    matrix[n - 1][n - 2] = h_n_1 / 6

    matrix[0][n] = (f[1][1] - f[0][1]) / h0 - Fx_0
    matrix[n - 1][n] = Fx_n - (f[n - 1][1] - f[n - 2][1]) / h_n_1



    for i in range(1, n-1):
        h0 = f[i][0] - f[i-1][0]
        h1 = f[i+1][0] - f[i][0]
        for j in range(0,n):
            if(i == j):
                matrix[i][j] = 1/3 * (h0 + h1)
                matrix[i][j-1] = 1/6 * h0
                matrix[i][j+1] = 1/6 * h1
        matrix[i][n] = (f[i+1][1] - f[i][1])/h1 - (f[i][1] - f[i-1][1])/h0

    print(np.array(matrix))
    result = gaussianElimination(matrix)
    if isinstance(result, str):
        print(result)
    else:
        print(bcolors.OKBLUE, "\nSolution for the system:")
        for x1 in result:
            print("{:.6f}".format(x1))


    build_s_printx0(f, x0, n, result)



if __name__ == '__main__':
    f = [(1, 1), (2, 2), (3, 1), (4, 1.5), (5, 1)]
    x0 = 6
    Fx_0 = 0
    Fx_n = 0

    print("func: " + str(f))
    print("x0 = " + str(x0) + "\n")
    natural_cubic_spline(f, x0)

