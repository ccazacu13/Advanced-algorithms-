n = int(input())
q = []


def viraj_dreapta(q):
    # 1            1           1
    # q[-3][0]  q[-2][0]    q[-1][0]
    # q[-3][1]  q[-2][1]    q[-1][1]
    det = q[-2][0] * q[-1][1] + q[-3][0] * q[-2][1] + q[-1][0] * q[-3][1] - q[-2][0] * q[-3][1] - q[-1][0] * q[-2][1] - q[-3][0] * q[-1][1]
    if det < 0 or det == 0:
        return True
    else:
        return False


for i in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    q.append((x, y))
    valid = True
    while valid and len(q) >= 3:
        if valid := viraj_dreapta(q):
            q.pop(-2)

if q:
    for i in range(2):
        elem = q[0]
        q.append(elem)

        valid = True
        while valid and len(q) >= 0:
            if valid := viraj_dreapta(q):
                q.pop(-2)
        q.pop(0)
        
print(len(q))
for x, y in q:
    print(x, y, sep=" ")