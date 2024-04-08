from colors import bcolors


def secant_method(f, x0, x1, TOL, N=50):
    print("{:<10} {:<15} {:<15} {:<15}".format("Iteration", "   xo", "   x1", "   x2"))
    for i in range(N):
        if f(x1) - f(x0) == 0:
            print( " method cannot continue.")
            return

        xr = (x0*f(x1) - x1*f(x0))/(f(x1) - f(x0))
        if abs(xr - x1) < TOL:
            return xr  # Procedure completed successfully
        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f}".format(i, x0, x1, xr))
        x0 = x1
        x1 = xr
    return xr


if __name__ == '__main__':
    f = lambda x: x**2 - 5*x +2
    x0 = 80
    x1 = 100
    TOL = 1e-6
    N = 20
    roots = secant_method(f, x0, x1, TOL, N)
    print(bcolors.OKBLUE, f"\n The equation f(x) has an approximate root at x = {roots}", bcolors.ENDC)
