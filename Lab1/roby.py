nr = int(input())

# points = [(int(tup[0]),int(tup[1])) for i in range(nr) if (tup := input().split()) ]
points = []
for i in range(nr):
    pos1, pos2 = input().split()
    pos1, pos2 = int(pos1), int(pos2)
    points.append((pos1, pos2))
left = 0
right = 0
touch = 0

for i in range(nr - 1):
    
    coords = []
    for num in range(i, i + 3):
        x, y = points[num % nr]
        coords.append(x)
        coords.append(y)
    
    det = coords[2]*coords[5] + coords[0]*coords[3] + coords[4]*coords[1] - coords[2]*coords[1] - coords[4]*coords[3] - coords[0]*coords[5]
    # print(coords)
    if not det:
        touch += 1
    elif det < 0:
        right += 1
    else: 
        left += 1

print(left, right, touch, end = " ")   




