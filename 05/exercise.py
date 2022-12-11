import csv

## exercise 01: which crates and up on top after the stacks have been moved?
##            : crates are move ONE AT A TIME (reversing ordering)
## exercise 02: same, but crates are moved in AT THE SAME time (keeping their ordering)

#exercise01: isReversed = True, exercise02: isReversed = False
isReversed = False

def reverseString(text):
  return text[::-1]

stacksDict = {}
with open('05/dataStacks.csv',newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        stacksNr = row[0].split(':')[0]
        stacksValues = row[0].split(':')[1]
        stacksDict.update( { int(stacksNr) : stacksValues } )
    print (stacksDict)
    
with open('05/dataMoves.csv',newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader: 
        #print(row[0])
        # process the steps
        tempString = row[0][5:len(row[0])]
        amount = int(tempString.split(' from ')[0])
        fromStack = int(tempString.split(' from ')[1].split(' to ')[0])
        toStack = int(tempString.split(' from ')[1].split(' to ')[1])
        
        fromString = stacksDict[fromStack]
        stacksDict.update( {fromStack : fromString[0:len(fromString)-amount]} )
        toString = stacksDict[toStack]
        appendString = fromString[-amount:]
        if(isReversed):
            appendString = reverseString(appendString)
        newString = toString + appendString
        stacksDict.update( {toStack : newString } )
        
    topCrates = ''
    for key in stacksDict:
        topCrates += stacksDict[key][-1]
    print(topCrates) 
        
        
        