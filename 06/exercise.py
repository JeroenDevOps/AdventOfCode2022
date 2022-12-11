import csv


## exercise 01: analyse the string to find the first 4-long combination without repeating characters, this will be the packet marker
## exercise 02: same as one but for a 14-long character string, this will be the message marker

# exercise01: stringLength = 4, exercise02: stringLength = 14
stringLength = 14 

with open('06/data.csv',newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')

    marker = 0
    for row in reader:
        inputString = row[0]
        for x in range(len(inputString)) :
            toAnalyse = inputString[x:x+stringLength]
            if(len(set(toAnalyse)) == len(toAnalyse)): # set doesn't allow for repeated values
                marker = x + stringLength
                break
    
    print(marker)

    