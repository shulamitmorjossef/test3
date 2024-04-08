from colors import bcolors


def linearInterpolation(table_points, point):
    flag = 1
    if (point < table_points[0][0]):
        i = 0
        flag = 0
    else:
        if (point > table_points[len(table_points) - 1][0]):
            i = len(table_points) - 2
            flag = 0
    if(not flag):
        x1 = table_points[i][0]
        x2 = table_points[1 + 1][0]
        y1 = table_points[i][1]
        y2 = table_points[i + 1][1]
        # m = (y1 - y2) / (x1 - x2)
        # result = y1 + m * (point - x1)
        result = ((point - x2) / (x1 - x2)) * y1 + ((point - x1) / (x2 - x1)) * y2

        print(bcolors.OKGREEN, "\nThe approximation (extrapolation) of the point ", point, " is: ", bcolors.ENDC,
              round(result, 4))
    else:
        p = []
        for i in range(len(table_points) - 1):
            if table_points[i][0] <= point <= table_points[i+1][0]:
                x1 = table_points[i][0]
                x2 = table_points[i + 1][0]
                y1 = table_points[i][1]
                y2 = table_points[i + 1][1]

                result = ((point - x2)/(x1-x2))*y1 + ((point - x1)/(x2-x1))*y2

                print(bcolors.OKGREEN, "\nThe approximation (interpolation) of the point ", point, " is: ",bcolors.ENDC, round(result, 4))


if __name__ == '__main__':

    table_points = [(0, 0), (1, 0.8415), (2, 0.9093), (3, 0.1411), (4, -0.7568), (5, -0.9589), (6, -0.2794)]

    x = 1.28
    print(bcolors.OKBLUE, "----------------- Interpolation & Extrapolation Methods -----------------\n", bcolors.ENDC)
    print(bcolors.OKBLUE, "Table Points: ", bcolors.ENDC, table_points)
    print(bcolors.OKBLUE, "Finding an approximation to the point: ", bcolors.ENDC, x)
    linearInterpolation(table_points, x)
    print(bcolors.OKBLUE, "\n---------------------------------------------------------------------------\n", bcolors.ENDC)



