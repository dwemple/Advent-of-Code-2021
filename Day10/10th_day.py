# The lack of a switch in python is breaking my heart, spaghetti here we go again
input = open("10th_day_input.txt", 'r')

temp = []
for item in input:
    temp.append(item.rstrip("\n"))

incomplete = temp.copy()
brackets = [0]*4
stack = []

# I should probably check if the line is corrupted or incomplete first
def part1():
    sum = 0
    for row in temp:
        for item in row:
            if item == '(' or item == '[' or item == '{' or item == '<':
                stack.insert(0, item)
                if item == '(':
                    brackets[0] += 1
                elif item == '[':
                    brackets[1] += 1
                elif item == '{':
                    brackets[2] += 1
                elif item == '<':
                    brackets[3] += 1
            else:
                if len(stack) != 0:
                    if item == ')' and stack[0] != '(':
                        incomplete.remove(row)
                        sum += 3
                        break
                    elif item == ']' and stack[0] != '[':
                        incomplete.remove(row)
                        sum += 57
                        break
                    elif item == '}' and stack[0] != '{':
                        incomplete.remove(row)
                        sum += 1197
                        break
                    elif item == '>' and stack[0] != '<':
                        incomplete.remove(row)
                        sum += 25137
                        break
                    stack.pop(0)
    return sum

def part2():

    stack = []
    rightstack = []
    sum = 0
    sumlist = []
    for row in incomplete:
        for item in row:   
            if item == '(' or item == '[' or item == '{' or item == '<':
                stack.insert(0, item)
            else:
                if len(stack) != 0:
                    if (item == ')' and stack[0] != '(' or 
                    item == ']' and stack[0] != '[' or
                    item == '}' and stack[0] != '{' or
                    item == '>' and stack[0] != '<'):
                        rightstack.insert(0, item)
                    else:
                        stack.pop(0)

        for char in stack:
            if len(rightstack):
                if char == '(' and rightstack[-1] != ')':
                    sum *= 5
                    sum += 1
                elif char == '[' and rightstack[-1] != ']':
                    sum *= 5
                    sum += 2
                elif char == '{' and rightstack[-1] != '}':
                    sum *= 5
                    sum += 3
                elif char == '<' and rightstack[-1] != '>':
                    sum *= 5
                    sum += 4
                else:
                    rightstack.pop(0)
            else:
                if char == '(':
                    sum *= 5
                    sum += 1
                elif char == '[':
                    sum *= 5
                    sum += 2
                elif char == '{':
                    sum *= 5
                    sum += 3
                elif char == '<':
                    sum *= 5
                    sum += 4
        rightstack = []
        stack = []
        sumlist.append(sum)
        sum = 0
    midIndex = len(sumlist) // 2
    return sorted(sumlist)[midIndex]

print("------------- Part1 -------------")
print(str(part1()))
print("------------- Part2 -------------")
print(part2())
