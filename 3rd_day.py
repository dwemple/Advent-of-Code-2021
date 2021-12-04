
trueCount = 0
falseCount = 0
gamma = 0
epsilon = 0

for i in range(11):
    input = open("3rd_day_input.txt", "r")
    print(str(i))
    for line in input:
        if line[11-i] == str(1):
            trueCount += 1
        else:
             falseCount += 1
    if trueCount > falseCount:
        print("Is bigger on index " + str(11-i) + "! True: " + str(trueCount) + ", false: " + str(falseCount))
        gamma += 2**(11-i)
    trueCount = 0
    falseCount = 0


epsilon = ~gamma & ((1 << 12) - 1)
print(format(gamma, "#014b"))
print(format(epsilon, "#014b"))
print(str(gamma) + " * " + str(epsilon) + " = " + str(gamma*epsilon))