from math import sqrt

def distance(a, b):
    # sqrt ( (Xa - Xb)^2 + (Ya - Yb)^2 )
    return sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]))


def viraj_dreapta(q):       # functie care calculeaza daca ultimele 3 puncte dintr-o lista fac un viraj la dreapta sau sunt coliniare
    # 1            1           1
    # q[-3][0]  q[-2][0]    q[-1][0]
    # q[-3][1]  q[-2][1]    q[-1][1]
    det = q[-2][0] * q[-1][1] + q[-3][0] * q[-2][1] + q[-1][0] * q[-3][1] - q[-2][0] * q[-3][1] - q[-1][0] * q[-2][1] - q[-3][0] * q[-1][1]
    if det < 0 or det == 0:
        return True
    else:
        return False


def convex_hull(arr):
    conv = []
    for point in arr:
        conv.append(point)

        while len(conv) >= 3 and viraj_dreapta(conv):
            conv.pop(-2)

    return conv

points = int(input())

arr_points = []

for i in range(points):
    x, y = input().split()
    arr_points.append((int(x),int(y)))

arr_points = sorted(arr_points, key=lambda b: (b[0], b[1]))

under = convex_hull(arr_points)
arr_points.reverse()
upper = convex_hull(arr_points)

convHull = under + upper[1:-1]

sums = [0 for i in range(points)]

while len(convHull) < points:
    pts = {}

    for point in arr_points:
        if point not in convHull:
            min = 9999
            length = len(convHull)
            for i in range(length):
                cost_ipj = distance(convHull[i], point) + distance(point, convHull[(i + 1) % length] )
                cost_ij = distance(convHull[i], convHull[(i + 1) % length] )
                sum = cost_ipj - cost_ij
                if sum < min:
                    pts[point] = (sum, i, cost_ipj / cost_ij)
                    min = sum

    min = 9999
    ind = ()
    for pct in pts.keys():
        division = pts[pct][2]
        if division < min:
            min = division
            ind = pct

    convHull.insert(pts[ind][1] + 1, ind)

print(convHull)