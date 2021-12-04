input = open("2nd_day_input.txt","r")
temp = 0
aim = 0
depth = 0
horizontal = 0
for line in input:
    if "forward" in line:
        horizontal += int(line.split(" ")[1])
        depth += aim*int(line.split(" ")[1])
    elif "down" in line:
        aim += int(line.split(" ")[1])
    else:
        aim -= int(line.split(" ")[1])

print("Horizontal: " +str(horizontal) + " and depth: " + str(depth) + " is = " + str(horizontal*depth))