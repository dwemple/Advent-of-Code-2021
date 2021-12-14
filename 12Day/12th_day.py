# i went and took a shower and it was still crunching numbers....takes an hour, works tho, uncomment second condition in the lowercase if


input = open("12th_day_input.txt")

templist = []
for item in input:
    h = item.split("-")
    s = h[1].strip("\n")
    templist.append(h[0])
    templist.append(s)


listSet = set(templist)
size = len(listSet) - 1
matrix = [[] for _ in range(size)]
matrix[0].append("start")
head = ["end"]


# Finds row with header 'head' and adds string to its row
def addToRow(head, string):
    for i in range(size):
        if len(matrix[i]) != 0:
            if head == matrix[i][0]:
                matrix[i].append(string)
                return

def addNewRow(head, string):
    for i in range(size):
        if len(matrix[i]) == 0:
            matrix[i].append(head)
            matrix[i].append(string)
            return
input.close()
input = open("12th_day_input.txt")

for item in input:
    temp = item.split("-")
    second = temp[1].strip("\n")
    for x in matrix:
        if len(x) != 0:
            head.append(x[0])
    
    if temp[0] == "start":
        matrix[0].append(second)
    else:
        if temp[0] in head:
            addToRow(temp[0], second)
        else:
            addNewRow(temp[0], second)
        if second in head:
            addToRow(second, temp[0])
        else:
            addNewRow(second, temp[0])

heads = [x[0] for x in matrix]
result = []
print(matrix)

# All other lowercase r max 1
def noOther(path, ay):
    flatten = set(path)
    for item in flatten:
        if item.islower():
            if path.count(item) > 2 and item == ay:
                return False
            if path.count(item) > 1 and item != ay:
                return False
    return True

i = 0
def dfSearch(head, path=[]):
    global result
    global i
    # find head and its row
    index = heads.index(head)
    if len(path) == 0:
        path.append("start")
    neighbors = matrix[index][1:]
    if "end" in neighbors:
        temp = path.copy()
        temp.append("end")
        result.append(temp)
    for item in neighbors:
        temp = path.copy()
        temp.append(item)
        if temp not in result:
            if item.islower():
                if temp.count(item) < 2:# or (noOther(temp, item) and item != "start" and item != "end"):
                    #f i < 5000:
                        dfSearch(item, temp)
            else:
                #if i < 5000:
                    dfSearch(item, temp)
        
            
print("------------- Part 1 --------------")

#print("The map:")
#for item in matrix:
#    print(item)
#print("-----------------------------------")

## Pathfinding 
dfSearch("start", [])
print("There's total of " + str(len(result)) + " possible paths.")

#for item in result:
#    print(item)
