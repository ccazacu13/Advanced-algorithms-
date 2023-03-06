nr = int(input())
out = []
for i in range(nr):
    line = input().split()
    coords = [int(nr) for nr in line]
    det = coords[2]*coords[5] + coords[0]*coords[3] + coords[4]*coords[1] - coords[2]*coords[1] - coords[4]*coords[3] - coords[0]*coords[5]
    if not det:
        out.append('TOUCH')
    elif det < 0:
        out.append('RIGHT')
    else:
        out.append('LEFT')

for response in out:
    print(response)
    
# 9 9 9
# 0 2 4
# 1 3 5