input = open("6th_day_input.txt")
fish = [0]*9

def countFish (days):
    for i in range(days):
        last = fish[0]
        for i in range(8):
            fish[i] = fish[i+1]

        fish[8] = last
        fish[6] += last
    temp = 0
    for i in range(9):
        temp += fish[i]
    return temp

for item in input:
    temp = item
    temp = temp.split(',')

state = [int(x) for x in temp]

for item in state:
    fish[item] += 1

print("Total fish in 80 days: " + str(countFish(80)))
print("Total fish in 256 days: " + str(countFish(256)))