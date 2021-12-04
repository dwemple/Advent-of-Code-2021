def checkBingo (card):
    if (all(x in card for x in ['0', '1' , '2', '3', '4']) or
    all(x in card for x in ['5', '6' , '7', '8', '9']) or
    all(x in card for x in ['10', '11' , '12', '13', '14']) or 
    all(x in card for x in ['15', '16' , '17', '18', '19']) or
    all(x in card for x in ['20', '21' , '22', '23', '24']) or
    all(x in card for x in ['0', '5' , '10', '15', '20']) or
    all(x in card for x in ['1', '6' , '11', '16', '21']) or
    all(x in card for x in ['2', '7' , '12', '17', '22']) or
    all(x in card for x in ['3', '8' , '13', '18', '23']) or
    all(x in card for x in ['4', '9' , '14', '19', '24'])) :
        return True

# 0  1  2  3  4 
# 5  6  7  8  9
#10 11 12 13 15
#15 16 17 18 19
#20 21 22 23 24
input = open("4th_day_input.txt")



calling = ""
bingo = ""
index = [""]*100
sum = [0]*100
final = 0
bruh = []

for i in range(100):
    bruh.append(i)

for i, line in enumerate(input):
    if i==0 :
        calling += line
    else:
        bingo += line
numbers = bingo.split()
count = len(numbers)
final = (count//25)

new = calling.split(",")

for j in range(final):
    for l in range(25):
        sum[j] += int(numbers[(j*25)+l])

print(numbers[(40*25):(40*25)+25])

def fun():
    for i, call in enumerate(new):
        for k in range(final):
            try:
                temp = numbers[(k*25):(k*25)+25].index(call)
            except ValueError:
                temp = -1
            if temp != -1:
                if k == 40:
                   print(call)
                index[k] += " " + str(temp)
                sum[k] -= int(numbers[(k*25)+temp])

            what = index[k].split()
            if checkBingo(what):
                if len(bruh) == 1:
                    if k == bruh[0]:
                        print("------------")
                        print("Last called number: " + call)
                        print("Sum: " + str(sum[k]))
                        return
                if k in bruh:
                    bruh.remove(k)
            
fun()
print(bruh[0])
