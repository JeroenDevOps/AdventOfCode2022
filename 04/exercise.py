import csv

with open('04/data.csv',newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    ## exercise 01: how many of the range pairs completely overlap (e.g. 2-10 overlaps 3-8 completely)?
    ## exercise 02: how many times is there any overlap? 
    totalCompleteOverlapPairs = 0
    totalPartialOverlapPairs = 0
    for row in reader:
        strings = row[0].split(',')
        string1a = int(strings[0].split('-')[0])
        string1b = int(strings[0].split('-')[1])
        string2a = int(strings[1].split('-')[0])
        string2b = int(strings[1].split('-')[1])
        
        if (string1a <= string2a and string1b >= string2b) or (string1a >= string2a and string1b <= string2b):
            totalCompleteOverlapPairs += 1
        elif (string1a < string2a and string1b > string2a) or (string1b > string2b and string1a < string2b) or (string1a == string2a) or (string1a == string2b) or (string1b == string2a) or (string1b == string2b) :
            totalPartialOverlapPairs += 1
            
    print('Total overlap: ', totalCompleteOverlapPairs)
    print('Partial overlap: ', totalPartialOverlapPairs)
    print('Total with overlap: ', totalPartialOverlapPairs + totalCompleteOverlapPairs)

    