input = open("1st_day_input.txt", "r")

firstTriple = 0
secondTriple = 0
thirdTriple = 0

firstCount = 0

firstCompare = 0
secondCompare = 0
thirdCompare = 0

temp = 0
triple = 0
tripleCount = 0
success = 0
wrong = 0
count = 0

for number in input: 
    temp = int(number)
    count += 1
    firstTriple += temp
    if triple == 3:
        firstCount += 1
        firstCompare = firstTriple
        firstTriple = 0
      # print("First: " + str(firstCompare))
          
    
    if  (triple == 1 and firstCount != 0) or triple == 2 or triple == 3:
        secondTriple += temp
        if triple == 1 and firstCount != 0:
            secondCompare = secondTriple
            secondTriple = 0
           # print("Second: " + str(secondCompare))


    if (triple == 1 and firstCount != 0) or (triple == 2 and firstCount != 0) or triple == 3:
        thirdTriple += temp
        if triple == 2 and firstCount != 0:
            thirdCompare = thirdTriple
            thirdTriple = 0
           # print("Third: " + str(thirdCompare))
            
 
    #Comparing first and second
    if triple == 1 and firstCount != 0:
        #print("Comparing if 2 > 1: " + str(secondCompare) + " > " + str(firstCompare))
        if secondCompare > firstCompare:
            success += 1
            #print(" > Success! 2 > 1")
        else:
           #print("Comparing if 2 > 1: " + str(secondCompare) + " > " + str(firstCompare))
            wrong += 1

        tripleCount += 1


    if triple == 2 and firstCount != 0:
        #print("Comparing if 3 > 2: " + str(thirdCompare) + " > " + str(secondCompare))
        if thirdCompare > secondCompare:
            success += 1
            print(" > Success! 3 > 2")
        else:
            #print("Comparing if 2 > 1: " + str(thirdCompare) + " > " + str(secondCompare))
            wrong += 1

        tripleCount += 1


    if triple == 3 and firstCount != 0:
        #print("Comparing if 1 > 3: " + str(firstCompare) + " > " + str(thirdCompare))
        if firstCompare > thirdCompare:
            success += 1
            #print(" > Success! 1 > 3")
        else:
            #print("Comparing if 2 > 1: " + str(firstCompare) + " > " + str(thirdCompare))
            wrong += 1
        tripleCount += 1
        triple = 0
        
    if count > 1997:
        print("whats wrong" + str(count))
        print("First: " + str(firstTriple) + ", second: " + str(secondTriple) + ", third: " + str(thirdTriple))

    triple += 1
    


print("Hmm? " + str(success) + " + " + str(wrong) + " = " + str(success+wrong))
print("Total triples: " + str(tripleCount))



