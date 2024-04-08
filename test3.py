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
#from Trapezoidal_method import trapezoidal_rule
from Trapezoidal_method import calc_trapez
from Simpson_method import simpsons_rule
from cubicSpline import natural_cubic_spline
from Romberg_method import romberg_integration
from lagrange_interpolation import lagrange_interpolation
from lagrange_interpolation import lagrange_interpolation



def output():
    print("Date:08/04/24\n"
          "Group members: \n"
          "(1) name: Shulamit-mor-yossef. id: 206576977. \n"
          "(2) name: Zohar-monsonego. id: 214067662. \n"
          "(3) name: hodaya-shirazie. id: 213907785.\n"
          "Git: https://github.com/shulamitmorjossef/test3.git\n"
          "Name: Shulamit Mor Yossef, 206576977.\n"

          "input:\n")
    table_points = [(1.2, -1.2), (1.3, -2.3), (1.4, -0.5), (1.5, 0.89), (1.6, 1.37)]
    x1 = 1.35
    x2 = 1.55
    print("Table points = ", table_points)
    print("\nxa = ", x1)
    print("xb = ", x2)

    f = lambda x: (3 * x ** 2 + math.sin(x ** 4 + 5 * x - 6)) / (2 * math.e ** (-2 * x + 5))
    # f = lambda x: (3 * x ** 2 + math.sin(x ** 4 + 5 * x - 6)) / (2 * math.e ** (-2 * x + 5))

    print("\nf(x) = 3*x^2 + sin(x^4 + 5*x - 6")
    print("      ---------------------------")
    print("           2 * e^(-2*x +5) ")




    print("\noutput:\n ")

    f1 = natural_cubic_spline(table_points, x1)
    f2 = natural_cubic_spline(table_points, x2)
    print("\nf(xa) = ", f1)
    print("f(xb) = ", f2)

    a=f1
    b=f2

    f = lambda x: (3 * x ** 2 + math.sin(x ** 4 + 5 * x - 6)) / (2 * math.e ** (-2 * x + 5))
    x1, x2 = 1.1, -1.5
    n1 = 120

    integralT =  trapezoidal_rule(f, x1, x2, n1)
    integralT1 = trapezoidal_rule(f, x1, x2, n1+1)

    print("\nApproximate integral in iteration" , n1, ":",  integralT)
    print("Approximate integral in iteration", n1+2, ":",  integralT1)




if __name__ == '__main__':

    output()
