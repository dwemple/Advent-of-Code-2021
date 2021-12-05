input=open("5th_day_input.txt")

field = [[0] * 1000 for i in range(1000)]
startx=0
starty=0
endx=0
endy=0

for n, line in enumerate(input):
    temp = line.split(" -> ")
    startx = int(temp[0].split(',')[0])
    starty = int(temp[0].split(',')[1])
    endx = int(temp[1].split(',')[0])
    endy = int(temp[1].split(',')[1])

#### Oh Neptune.........
    if endx > startx and starty==endy: # [X2 > X1, Y1==Y2] 0,9 -> 5,9 | 0,9 -> 2,9
        for i in range(endx-startx+1):
            #print("Add 1 to coordinate: X= " + str(startx+i) + " | Y= " + str(starty))
            field[(startx+i)][starty] += 1
            #print(str(startx+i) + "," + str(starty) + " -> " + str(field[(startx+i)][starty]))
    elif startx > endx and starty==endy: # [X1 > X2, Y1==Y2] 9,4 -> 3,4 | 3,4 -> 1,4
        for i in range(startx-endx+1):
            field[endx+i][starty] += 1
    elif endy > starty and endx == startx: # [Y2 > Y1, X1==X2] 2,2 -> 2,1
        for k in range(endy-starty+1):
            field[endx][starty+k] += 1
    elif starty > endy and endx == startx: # [Y1 > Y2, X1==X2] 7,0 -> 7,4
        for k in range(starty-endy+1):
            field[endx][endy+k] += 1
    elif starty==startx and endy==endx and startx != endx: # [X1==Y1, X2==Y2, X1 != X2]
        if starty > endy: # [Y1 > Y2]
            for i in range(starty-endy+1):
                field[endy+i][endy+i] += 1
        else: # [Y2>Y1]
            for i in range(endy-starty+1):
                field[starty+i][starty+i] += 1
    elif startx == endy and starty==endx: # [X1 == Y2, Y1 == X2]
        if startx > starty: # [X1 > Y1] 8,0 -> 0,8
            for i in range(startx-starty+1):
                field[startx-i][starty+i] +=  1
        else: # [Y1 < X1]
            for i in range(starty-startx+1):
                field[starty-i][startx+i] += 1
    elif starty==startx and endy==endx and startx == endx: # X1==X2==Y1==Y2
        field[endx][endy] += 1
    elif abs(startx-endx) == abs(starty-endy): # 710,499 -> 451,758
        if endx > startx and endy > starty: # X++ Y++
            for i in range(endx - startx + 1):
                field[startx+i][starty+i] += 1
        elif startx > endx and starty > endy: # X-- Y-- ??? 6,4 -> 2,0
            for i in range(startx - endx + 1):
                field[startx-i][starty-i] += 1
        elif endx > startx and starty > endy: # X++ Y--
            for i in range(endx - startx + 1):
                field[startx+i][starty-i] += 1
        elif startx > endx and endy > starty: # X-- Y++
            for i in range(startx - endx + 1):
                field[startx-i][starty+i] += 1

count = 0
for item in field:
    for number in item:
        if number > 1:
            count +=1
print(str(count))