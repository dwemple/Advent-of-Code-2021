input = open("3rd_day_input.txt")

oxygen = []
nitrogen = []
def filterList(index, char, list):
    result = []
    for item in list:
        if item[index] == char:
            result.append(item)
    return result

def getBiggerSum(listToFilter):
    ones = [0]*12
    zeros = [0]*12
    for item in listToFilter:
        for i, char in enumerate(item):
            if char == '1':
                ones[i] += 1
            else:
                zeros[i] += 1
    return ones, zeros

gamma = ""
epsilon = ""
ones = [0]*12
zeros = [0]*12
oxy = ""
nitro = ""
for item in input:
    nitrogen.append(item.rstrip("\n"))
    oxygen.append(item.rstrip("\n"))
    for i, char in enumerate(item.rstrip("\n")):
        if char == '1':
            ones[i] += 1
        else:
            zeros[i] += 1

for i in range(12):
    if ones[i] > zeros[i]:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'


oxyOnes, oxyZeros = getBiggerSum(oxygen)
nitroOnes, nitroZeros = getBiggerSum(nitrogen)

for i in range(12):
    if oxyOnes[i] == oxyZeros[i]:
        oxygen = filterList(i, '1', oxygen)
    elif oxyOnes[i] > oxyZeros[i]:
        if len(oxygen) > 1:
            oxygen = [item for item in oxygen if item not in filterList(i, '0', oxygen)]
    else:
        if len(oxygen) > 1:
            oxygen = [item for item in oxygen if item not in filterList(i, '1', oxygen)]
    oxyOnes, oxyZeros = getBiggerSum(oxygen)

    if nitroOnes[i] == nitroZeros[i]:
        nitrogen = filterList(i, '0', nitrogen)
    elif nitroOnes[i] < nitroZeros[i]:
        if len(nitrogen) > 1:
            nitrogen = [item for item in nitrogen if item not in filterList(i, '0', nitrogen)]
    else:
        if len(nitrogen) > 1:
            nitrogen = [item for item in nitrogen if item not in filterList(i, '1', nitrogen)]

    nitroOnes, nitroZeros = getBiggerSum(nitrogen)

result = int(gamma, 2) * int(epsilon, 2)
print("Part 1: " + str(int(gamma,2)) + " * " + str(int(epsilon,2)) + " = " + str(result))


result = int(oxygen[0], 2) * int(nitrogen[0], 2)
print("Part 2: " + str(int(oxygen[0], 2)) + " * " + str(int(nitrogen[0], 2)) + " = "  + str(result))