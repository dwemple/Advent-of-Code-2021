input = open("14th_day_input.txt")

firstline = ""
rules = []
temp = []
for i, line in enumerate(input):
    if i == 0:
        firstline = line.rstrip("\n")
    elif line != "\n":
        temp.append(line.rstrip("\n"))
        rules += temp[i-2].split(" -> ")

temp = []
duo = []

for i in rules:
    if len(i) == 1:
        temp.append(i)
    else: 
        duo.append(i)

tempset = set(temp)
tempduoset = set(duo)

counterS = [[] for _ in range(len(tempset))]
counterD = [[] for _ in range(len(tempduoset))]

def getRule(syllable):
    for i, item in enumerate(rules):
        if item == syllable:
            return rules[i+1]

for i, item in enumerate(counterS):
    counterS[i].append(list(tempset)[i])
    counterS[i].append(0)
for i, item in enumerate(counterD):
    counterD[i].append(duo[i])
    counterD[i].append(getRule(duo[i]))
    counterD[i].append(0)


def addLetterCount(letter, x):
    for i in range(len(counterS)):
        if counterS[i][0] == letter:
            counterS[i][1] += x

def addSyllableCount(syllable):
    for i in range(len(counterD)):
        if counterD[i][0] == syllable:
            return i

# Chomp:
for i in range(len(firstline)):
    d = firstline[i:i+2]
    for x, item in enumerate(counterD):
        if counterD[x][0] == d:
            counterD[x][2] += 1
    addLetterCount(firstline[i],1)
def nyom(part):
    for _ in range(part):
        newCounter = [[i for i in row] for row in counterD]
        for i in range(len(newCounter)):
            newCounter[i][2] = 0
        for x in range(len(newCounter)):
            if counterD[x][2] > 0:
                many = counterD[x][2]
                counterD[x][2] = 0
                a = counterD[x][0][0] + counterD[x][1]
                b = counterD[x][1] + counterD[x][0][1]
                newCounter[addSyllableCount(a)][2] += many
                newCounter[addSyllableCount(b)][2] += many
                addLetterCount(counterD[x][1], many)
        for i in range(len(newCounter)):
            counterD[i][2] = newCounter[i][2]
    final = []
    for i, item in enumerate(counterS):
        final.append(counterS[i][1])
    return final

part1 = nyom(10)
part2 = nyom(40)

print(str(max(part1)) + " - " + str(min(part1)) + " = " + str(max(part1)-min(part1)))
print(str(max(part2)) + " - " + str(min(part2)) + " = " + str(max(part2)-min(part2)))