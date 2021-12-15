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


def addLetterCount(letter):
    for i in range(len(counterS)):
        if counterS[i][0] == letter:
            counterS[i][1] += 1

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
    addLetterCount(firstline[i])

for _ in range(10):
    newCounter = [[i for i in row] for row in counterD]
    for i in range(len(newCounter)):
        newCounter[i][2] = 0
    for i in range(len(rules) // 2):
        for x in range(len(newCounter)):
            if counterD[x][2] > 0 and counterD[x][0] == rules[i*2]:
                many = counterD[x][2]
                for _ in range(many):
                    counterD[x][2] -= 1
                    a = counterD[x][0][0] + rules[i*2+1]
                    b = rules[i*2+1] + counterD[x][0][1]
                    newCounter[addSyllableCount(a)][2] += 1
                    newCounter[addSyllableCount(b)][2] += 1
                    addLetterCount(rules[i*2+1])
    for i in range(len(newCounter)):
        counterD[i][2] = newCounter[i][2]

final = []
for i, item in enumerate(counterS):
    final.append(counterS[i][1])

max = max(final)
min = min(final)

print(str(max) + " - " + str(min) + " = " + str(max-min))