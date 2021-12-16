# pathfinding is the biggest pain in the ass

input = open("15th_day_input.txt")

matrix = [[] for _ in range(10)]
for r, line in enumerate(input):
    for x in line.rstrip("\n"):
        matrix[r].append(int(x))

# check neighbors
# start at 0,0
r = 0
c = 0
def idk(r,c, back, path=[]):
    smallest = 0
    if r == 10 and c == 10:
        return path
    topV, downV, leftV, rightV = 0, 0, 0, 0
    if r - 1 > 0 and back != "top":
        topV = matrix[r-1][c]
    if r + 1 < 10 and back != "down":
        downV = matrix[r+1][c]
    if c - 1 > 0 and back != "left":
        leftV = matrix[r][c-1]
    if c + 1 < 10 and back != "right":
        rightV = matrix[r][c+1]
    return idk





for line in matrix:
    print(line)
