input = open("16th_day_input.txt")
for item in input:
    hex = item.rstrip("\n")

def hexToBin(hexadeciaml):
    binary = ""
    for digit in hexadeciaml:
        # switcherino
        if digit == '0':
            binary += "0000"
        elif digit == '1':
            binary += "0001"
        elif digit == '2':
            binary += "0010"
        elif digit == '3':
            binary += "0011"
        elif digit == '4':
            binary += "0100"
        elif digit == '5':
            binary += "0101"
        elif digit == '6':
            binary += "0110"
        elif digit == '7':
            binary += "0111"
        elif digit == '8':
            binary += "1000"
        elif digit == '9':
            binary += "1001"
        elif digit == 'A':
            binary += "1010"
        elif digit == 'B':
            binary += "1011"
        elif digit == 'C':
            binary += "1100"
        elif digit == 'D':
            binary += "1101"
        elif digit == 'E':
            binary += "1110"
        elif digit == 'F':
            binary += "1111"
    return binary

ban = hexToBin(hex)

def binToDec(binary):
    if binary == "":
        return 0
    else:
        return int(binary,2)

#print(ban)
bList = []
rList = []
total, result = 0 ,0

def doMagic(x):
    print(rList)
    print(bList)

    result = 0
    if len(rList) > 1:
        if x == 0:
            for value in rList:
                result += value
        elif x == 1:
            result = rList[0]
            for r, value in enumerate(rList):
                if r != 0:
                    result *= value
        elif x == 2:
            result = min(rList)
        elif x == 3:
            result = max(rList)
        elif x == 5:
            if rList[0] > rList[1]:
                result = 1
            else:
                result = 0
        elif x == 6:
            if rList[0] < rList[1]:
                result = 1
            else:
                result = 0
        elif x == 7:
            if rList[0] == rList[1]:
                result = 1
            else:
                result = 0
        rList.clear()
    else:
        if x == 0:
            for value in bList:
                result += value
        elif x == 1:
            print(bList)
            result = bList[0]
            for r, value in enumerate(bList):
                if r != 0:
                    result *= value
        elif x == 2:
            result = min(bList)
        elif x == 3:
            result = max(bList)
        elif x == 5:
            if bList[0] > bList[1]:
                result = 1
            else:
                result = 0
        elif x == 6:
            if bList[0] < bList[1]:
                result = 1
            else:
                result = 0
        elif x == 7:
            if bList[0] == bList[1]:
                result = 1
            else:
                result = 0
    bList.clear()
    return result

def getValue(string):
    lenght = 0
    ret, sum = "",""
    i = 0
    for x in range(len(string)//5):
        sum += string[x*5:5+x*5]
        if string[x*5] == '0':
            break
        i += 1
    lenght = len(string[:5+i*5])
    ret = string[5+i*5:]
    return lenght+6, ret, binToDec(sum)

def chopchop(binary):
    global total, result, bList
    ret = ""
    lenght = 0
    packetV = binToDec(binary[0:3])
    packetT = binToDec(binary[3:6])
    total += packetV
    print("Packet value: " + str(packetV) + ", " + binary[0:3])
    print("Packet type: " + str(packetT) + ", " + binary[3:6])
    print("---")
    if packetT == 4:
        binary = binary[6:]
        lenght, ret, temperino = getValue(binary)
        bList.append(temperino)
    else:
        if binary[6] == '0':
            # Lenght type ID 0 => next 15b
            lenght = binToDec(binary[8:22])
            binary = binary[22:]
            copyr = binary
            copyl = lenght
            while lenght > 0:
                delet, binary = chopchop(binary)
                lenght -= delet
            rList.append(doMagic(packetT))
            ret = copyr[copyl:]
            lenght = copyl+22
        else:
            # Lenght type ID 1 => next 11b
            count = binToDec(binary[8:18])
            delet = 18
            binary = binary[delet:]
            for _ in range(count):
                delet, binary = chopchop(binary)
                lenght += delet
            # Packet types
            rList.append(doMagic(packetT))
            lenght += 18
            ret = binary

    return lenght, ret

print("-------- Part 1 --------")
chopchop(ban)
print("------------------------")
print("Sum of version numbers: " + str(total))
print("-------- Part 2 --------")
print("Result is: " + str(rList))