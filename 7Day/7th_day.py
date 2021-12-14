input = open("7th_day_input.txt")
median = 0
for item in input:
    temp = item
temp = temp.split(",")

state = [int(x) for x in temp]
for item in state:
    median += item

median = round((median/len(state)))

def countChangeExponential(x):
    sum = 0
    for item in state:
        for i in range(abs(item-x)):
            sum += 1+i
    return sum

def countChange(x):
    sum = 0
    for item in state:
        sum += abs(item-x)
    return sum

print("------------------- Day 7 - crab submarines? -------------------")


smallest = 0
smallest = countChange(median)
smaller = median

for i in range(50):
    if countChange(median-i) < smallest:
        smaller = median-i
        smallest = countChange(median-i)
    if countChange(median+i) < smallest:
        smallest = countChange(median+i)
        smaller = median+i

print("Part 1 -- Position: " + str(smaller) + ", fuel used: " + str(smallest))

smallest = 0
smallest = countChangeExponential(median)
smaller = median

for i in range(5):
    temp1 = countChangeExponential(median-i)
    temp2 = countChangeExponential(median+i)
    if temp1 < smallest:
        smaller = median-i
        smallest = temp1
    if temp2 < smallest:
        smallest = temp2
        smaller = median+i

print("Part 2 -- Position: " + str(smaller) + ", fuel used: " + str(smallest))
print("----------------------------------------------------------------")