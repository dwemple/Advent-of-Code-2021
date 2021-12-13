input = open("11th_day_input.txt")
max = 10
temp = [[]*10 for _ in range(10)]
for i, item in enumerate(input):
    row = item.strip("\n")
    for digit in row:
        temp[i].append(int(digit))
    row = ""

count = 0
after = 0
first = False
def showArray():
    for item in temp:
        print(item)

def checkOnPos(r,c):
    global count
    if temp[r][c] != 9:
        temp[r][c] += 1
    else:
        temp[r][c] = 10
        flash(r, c)
        count += 1

def flash(r,c):
    if r-1 >= 0:
        if c-1 >= 0:
            checkOnPos(r-1, c-1)
        if c+1 < max:
            checkOnPos(r-1, c+1)
        checkOnPos(r-1, c)
    if r+1 < max:
        if c-1 >= 0:
            checkOnPos(r+1, c-1)
        if c+1 < max:
            checkOnPos(r+1, c+1)
        checkOnPos(r+1, c)
    if c-1 >= 0:
        checkOnPos(r, c-1)
    if c+1 < max:
        checkOnPos(r, c+1)


loop = [[0]*10 for _ in range(10)]

for i in range(1000):
    for r, row in enumerate(temp):
        for c, digit in enumerate(row):
            if temp[r][c] != 9:
                temp[r][c] += 1
            else:
                loop[r][c] = 1
                    
    for r, row in enumerate(loop):
            for c, digit in enumerate(row):
                if digit == 1:
                    checkOnPos(r,c)

    for r, row in enumerate(temp):
        for c, digit in enumerate(row):
            loop[r][c] = 0
            if temp[r][c] > 9:
                temp[r][c] = 0

    if first == False:
        if (count - after) == 100:
            print("All flashes at step: " + str(i+1))
            first= True
    after = count

print(str(count))

