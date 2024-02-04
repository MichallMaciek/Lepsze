import time

la = [[1, 1, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [1, 1, 1, 1, 1],
     [1, 0, 0, 0, 0],
     [1, 0, 0, 0, 0]]

# la = [[0, 1, 0, 0, 0],
#      [0, 1, 1, 0, 0],
#      [0, 1, 1, 0, 0],
#      [1, 1, 1, 0, 0],
#      [1, 0, 0, 0, 0]]

# la = [[1, 0, 0, 0, 0],
#      [1, 0, 1, 1, 1],
#      [1, 0, 1, 0, 1],
#      [1, 1, 1, 0, 1],
#      [0, 0, 0, 0, 1]]

# la = [[1, 0, 0, 0, 0],
#      [1, 1, 1, 1, 1],
#      [1, 0, 1, 0, 1],
#      [1, 0, 1, 0, 1],
#      [0, 0, 0, 0, 1]]


n = len(la)

def distance(p1, p2):
    if type(p1) == tuple and len(p1) == 2:
        p1x, p1y = p1
        if type(p2) == tuple and len(p2) == 2:
            p2x, p2y = p2
            return abs(p1x - p2x) + abs(p1y - p2y) == 1
    return False

def rm(p1):
    for _, __ in path.items():
        if p1 in __:
            __.remove(p1)
            path[_] = __

def rmodga():
    f = True
    while f:
        l = []
        for jj, j in path.items():
            if len(j) == 1 and jj[1] != 0 and jj[1] != 4 and jj not in prepositions:
                rm(jj)
                path.pop(jj)
                l.append(False)
                break
            else:
                l.append(True)
        if all(l):
            f = False

positions = []

for i, j in enumerate(la):
    points = [(_, i) for _ in range(n) if j[_] == 1]
    print(j, points)
    positions += points

print()
print(f"positions {positions}")

path = {}

for i, j in enumerate(positions):
    for k in range(len(positions)-1, -1, -1):
        if distance(j, positions[k]):
            # print(j, positions[k])
            if j not in path.keys():
                path[j] = [positions[k]]
            else:
                path[j].append(positions[k])

print()
print(f"path")

print()
temp = positions[0]
prepositions = [temp]
positions.remove(temp)

for _ in path.items():
    print(_)

rmodga()

while prepositions[-1][-1] + 1 < n:
    if len(path[temp]) == 2:
        rmodga()
    rm(temp)
    temp = path.pop(temp)[0]
    positions.remove(temp)
    prepositions.append(temp)

print()
print(f"prepositions {prepositions}")






