import numpy as np
import colors as bcolors
import math


# from matrix_utility import ...

from inverse_matrix import inverse
from gauss_seidel import gauss_seidel
from Jacobi import jacobi_iterative

from lu import lu
from lu import backward_substitution
from lu import lu_solve

from gaussian_elimination import gaussianElimination
from gaussian_elimination import backward_substitution
from gaussian_elimination import forward_substitution


from condition_of_linear_equations import condition_number
from condition_of_linear_equations import norm

from iterative_method import find_roots_iterative_method
from iterative_method import iterative_method
from bisection_method import bisection_method
from newtonRaphson import newton_raphson
from secant_method import secant_method
from linear_interpolation import linearInterpolation
from polynomial_interpolation import polynomialInterpolation
from Trapezoidal_method import trapezoidal_rule
from Simpson_method import simpsons_rule
from cubicSpline import natural_cubic_spline
from Romberg_method import romberg_integration
from lagrange_interpolation import lagrange_interpolation


def output():
    print("Date:08/04/24\n"
          "Group members: \n"
          "(1) name: Shulamit-mor-yossef. id: 206576977. \n"
          "(2) name: Zohar-monsonego. id: 214067662. \n"
          "(3) name: hodaya-shirazie. id: 213907785.\n"
          "Git: https://github.com/shulamitmorjossef/test2-shulamit.git\n"
          "Name: Shulamit Mor Yossef, 206576977.\n"

          "input:    \n[[-1, 1, 3, -3, 1,3],\n"
           "[3, -3, -4, 2, 3, 8],\n"
           "[2, 1, -5, -3, 5, 2],\n"
           "[-5, -6, 4, 1, 3, 14],\n"
           "[3, -2, -2, -3, 5, 6]]\n")
    print("(e * x ** 5 - 3 * x ** 3 + 2 * x ** 2 + 1)\n"
          "------------------------------------------\n"
          "               3 * x")
    print("\noutput:\n ")
    print("The matrix solution: \n")


    A_b = [[-1, 1, 3, -3, 1,3],
           [3, -3, -4, 2, 3, 8],
           [2, 1, -5, -3, 5, 2],
           [-5, -6, 4, 1, 3, 14],
           [3, -2, -2, -3, 5, 6]]
    result = gaussianElimination(A_b)
    if isinstance(result, str):
        print(result)
    else:
        print("Solution for the system:")
        for x in result:
            print("{:.6f}".format(x))



    print("\nThe roots: ")
    f = lambda x: (math.exp(1) * x ** 5 - 3 * x ** 3 + 2 * x ** 2 + 1) / 3 * x


    roots = bisection_method(f, -2, 0)
    print(f"\nRoot: {roots}")


    roots = bisection_method(f, 1, 2)
    if(roots != None):
        print(f"\nRoot: {roots}")


    try:
        for i in range(-2, 0, 1):
            initial_guess = i
            root, iterations = iterative_method(f, initial_guess, -2, 2)  # Adjust lower and upper bounds as needed
            if root is not None:
                print(f"\nRoot:", root)

    except ValueError as e:
        print(str(e))


    try:
        for i in range(1, 2, 1):
            initial_guess = i
            root, iterations = iterative_method(f, initial_guess, -2, 2)  # Adjust lower and upper bounds as needed
            if root is not None:
                print(f"\nRoot:", root)

    except ValueError as e:
        print(str(e))


    return


if __name__ == '__main__':

    output()
