input = open("13th_day_input.txt")
xlist = []
ylist = []
fold = []

maxY = 447*2 + 1
maxX = 655*2 + 1

twoD = [[] for i in range(maxY)]
for i in range(maxX):
    for x in range(len(twoD)):
        twoD[x].append('')

for item in input:
    if item.startswith('f'):
        temp = item.split(" ")
        lol = temp[2].split("=")
        fold.append(lol)
    else:
        if item != "\n":
            temp = item.split(",")
            x = int(temp[0])
            y = int(temp[1].strip("\n"))
            twoD[y][x] = '#'

def foldMatrix(axis, number, matrix):
    maxColumn = len(matrix[0])
    maxRow = len(matrix)
    if axis == 'y':
        newMatrix = [[] for _ in range(number)]
        for i in range(number):
            for x in range(maxColumn):
                newMatrix[i].append(' ')
        for y, row in enumerate(matrix):
            for x, digit in enumerate(row):
                if y > number:
                    if digit == '#':
                        newMatrix[abs(y - (maxRow - 1))][x] = '#'
                else:
                    if digit == '#':
                        newMatrix[y][x] = '#'
    if axis == 'x':
        newMatrix = [[] for _ in range(maxRow)]
        for i in range(maxRow):
            for x in range(number):
                newMatrix[i].append(' ')
        for y, row in enumerate(matrix):
            for x, digit in enumerate(row):
                if x > number:
                    if digit == '#':
                        newMatrix[y][abs(x - (maxColumn - 1))] = '#'
                else:
                    if digit == '#':
                        newMatrix[y][x] = '#'
    return newMatrix


count = 0
bruh = twoD.copy()

for i, item in enumerate(fold):
    temp = foldMatrix(fold[i][0], int(fold[i][1]), bruh)
    if i == 0:
        for line in temp:
            count += line.count('#')
        print("Part 1 : " + str(count))
    bruh = temp.copy()

for line in temp:
    print(line)