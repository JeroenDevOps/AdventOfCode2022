import csv

with open('03/data.csv',newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    
    # for row in reader:
    #     print(row)
    
    ## exercise 01: get the duplicate items (character) in the first and latter half of the string
    ##              give the item score sum (items: a-z = 0-26, A-Z = 27-52)
    charScores = {
        'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 
        'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26,
        'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 
        'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52          
                }
    
    totalScore = 0
    for row in reader:
        compartmentLength = int(len(row[0]) / 2)
        compartmentA = row[0][0:compartmentLength]
        compartmentB = row[0][-compartmentLength:compartmentLength*2]
        
        for x in range(len(compartmentA)) :
            if row[0][x] in compartmentB :
                #print('for row: ', row[0], ' the duplicate is: ', row[0][x])
                totalScore += charScores[row[0][x]]
                break
    
    print(totalScore)
                

    

with open('03/data.csv',newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    
    ## exercise 02: every 3 lines are 1 group and have one corresponding item 
    ##              return the sum of the item scores of each 3-man group
    stringList = []
    totalGroupedScore = 0
    for row in reader:
        stringList.append(row[0])
        
    # loop over the stringList with an increment of 3
    for x in range(0,len(stringList),3): 
        # retrieve longest string from the group of three
        string1 = stringList[x]
        string2 = stringList[x+1]
        string3 = stringList[x+2]
        
        stringToUse = ''
        if len(string1) > len(string2) and len(string1) > len(string3):
            stringToUse = string1
        elif len(string2) > len(string1) and len(string2) > len(string3):
            stringToUse = string2
        else:
            stringToUse = string3
        
        # find the common character and add its value to the total score
        for y in range(len(stringToUse)):
            if stringToUse[y] in string1 and stringToUse[y] in string2 and stringToUse[y] in string3:
                #print('group ', x, ' letter is: ', stringToUse[y], ' with ', charScores[stringToUse[y]], ' points.')
                totalGroupedScore += charScores[stringToUse[y]]
                break
                
    print(totalGroupedScore)    
        