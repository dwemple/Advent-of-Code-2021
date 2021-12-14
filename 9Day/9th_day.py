# Did someone order spaghetti
# This sure is a mess but it works !

input = open("9th_day_input.txt")
temp = []
for item in input:
    temp.append(item.rstrip("\n"))

lowest = []
basins = []

# It fucks up part1 if I don't use a copy
temperino = temp.copy()

# Come through recursive functions ! Boots the house down

def part2(r,c,top,bottom,right,left):
    basinsList = ""
    if top:
        top = r-1 != -1
        if top and temperino[r-1][c] != '9':
            basinsList += part2(r-1, c, top, False, right, left)
    if left:
        left = c-1 != -1
        if left and temperino[r][c-1] != '9':
            basinsList += part2(r, c-1, top, bottom, False, left)
    if bottom:
        bottom = r+1 != len(temp)
        if bottom and temperino[r+1][c] != '9':
            basinsList += part2(r+1, c, False, bottom, right, left)
    if right:
        right = c+1 != len(temp[0])
        if right and temperino[r][c+1] != '9':
            basinsList += part2(r, c+1, top, bottom, right, False)
    if temperino[r][c] != '9':
        # String work magic in python whew
        basinsList += temperino[r][c]
        templist = list(temperino[r])
        templist[c] = ' '
        temperino[r]= ''.join(templist) 
    return basinsList

for i, row in enumerate(temp):
    rowSize = len(row)
    for n, digit in enumerate(row):
        top, left, right, bottom = '0','0','0','0'
        if i == 0:
            top = "11"
        if i == len(temp)-1:
            bottom = "11"
        if n == 0:
            left = "11"
        if n == len(row)-1:
            right = "11"
        if top == '0':
            top = temp[i-1][n]
        if bottom == '0':
            bottom = temp[(i+1)][n]
        if left == '0':
            left = row[n-1]
        if right == '0':
            right = row[n+1]
        if digit:
            if int(digit) < int(top) and int(digit) < int(bottom) and int(digit) < int(right) and int(digit) < int(left):
                #print("Smallest is '" + digit + "', smaller than: t:" + top + " b:" + bottom + " l:" + left + " r:" + right)
                lowest.append(int(digit))
                basins.append(part2(i,n,top != "11",bottom != "11",right != "11",left != "11"))




print("------------- Part1 -------------")
part1 = 0
for i in lowest:
    part1 += i+1
print("Sum of the lowest points in the area is " + str(part1))

print("------------- Part2 -------------")
one, two, three = 0, 0, 0 
for i in basins:
    lenght = len(i.replace(" ", ""))
    if lenght > one:
        one = lenght
    elif lenght > two:
        two = lenght
    elif lenght > three:
        three = lenght

print("I don't even know man " + str(one) + " * " + str(two) + " * " + str(three) + " = " + str(one*two*three))