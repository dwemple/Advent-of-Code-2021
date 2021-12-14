# what an ugly ass code lmaoo

def printHelp(string):
    print(" " + string[0] + string[0] + string[0] + " ")
    print(string[1] + "   " + string[2])
    print(string[1] + "   " + string[2])
    print(" " + string[3] + string[3] + string[3] + " ")
    print(string[4] + "   " + string[5])
    print(string[4] + "   " + string[5])
    print(" " + string[6] +  string[6] + string[6] + " ")

def removeChar(src, toRemove):
    for char in toRemove:
        src = src.replace(char, '')
    return src

def part1():
    count = 0
    for item in temp:
        lol = item.split('|')
        huh = lol[1].split(' ')
        for string in huh:
            if len(string) == 2 or len(string) == 3 or len(string) == 4 or len(string) == 7:
                count += 1
    return count

def part2():
    sum = 0
    for item in temp:
        result = ""
        five = []
        six = []
        code = ['.']*7
        lol = item.split('|')
        first = lol[0].split(' ')
        second = lol[1].split(' ')
        for string in first:
            if len(string) == 3:
                seven = string
            if len(string) == 4:
                four = string
            if len(string) == 2:
                one = string
            if len(string) == 7:
                eight = string
            if len(string) == 5:
                five.append(string)
            if len(string) == 6:
                six.append(string)

        code[0] = removeChar(seven, one)

        for item5 in five:
            temp5 = removeChar(item5, one)
            if len(temp5) == 3: #je to 3
                temp5 = temp5.replace(code[0], '')
                if four.find(temp5[0]) != -1:
                    code[3] = temp5[0]
                    code[6] = temp5[1]
                else:
                    code[6] = temp5[0]
                    code[3] = temp5[1]
                five.remove(item5)
        code[1] = removeChar(four, one + code[3])
        for item6 in six:
            temp60 = item6.replace(one[0], '')
            temp61 = item6.replace(one[1], '')
            if len(temp60) == 6: #je to 6 a one[0] je 2
                code[2] = one[0]
                code[5] = one[1]
            elif len(temp61) == 6:
                code[5] = one[0]
                code[2] = one[1]
        code[4] = removeChar(eight, code)

        for string in second:
            if len(string) == 3:
                result += '7'
            if len(string) == 4:
                result += '4'
            if len(string) == 2:
                result += '1'
            if len(string) == 7:
                result += '8'
            if len(string) == 5:
                if len(removeChar(string, seven + code[3] + code[6])) == 0:
                    result += '3'
                elif len(removeChar(string, code[0] + code[1] + code[3] + code[5] + code[6])) == 0:
                    result += '5'
                else:
                    result += '2'
            if len(string) == 6:
                if len(removeChar(string, code[3])) == 6:
                    result += '0'
                elif len(removeChar(string, code[4])) == 6:
                    result += '9'
                else:
                    result += '6'
        sum += int(result)
    return sum


input = open("8th_day_input.txt")

temp = []
for item in input:
    temp.append(item.rstrip('\n'))


print("Total sum of 1, 4, 7, 8 is: " + str(part1()))
print("Total sum of the output: " + str(part2()))
