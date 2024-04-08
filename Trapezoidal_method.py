import math
import sympy as sp
from sympy.utilities.lambdify import lambdify
from colors import bcolors


def trapezoidal_rule(f, a, b, n):

    h = (b - a) / n
    T = f(a) + f(b)
    integral = 0.5 * T

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)

    integral *= h

    return integral


if __name__ == '__main__':
    f = lambda x: (3 * x ** 2 + math.sin(x ** 4 + 5 * x - 6)) / (2 * math.e ** (-2 * x + 5))
    x1, x2 = 1.1, -1.5
    n1 = 200



    result = trapezoidal_rule(f, x1, x2, n1)
    print(bcolors.OKBLUE,"n=" + str(n1))

    print(bcolors.OKBLUE, "Approximate integral:", result, bcolors.ENDC)
