import csv


with open('01/data.csv',newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    
    valueByIterationMap = {};  
    iteration = 1;
    
    for row in reader:
        if len(row) == 0:
            iteration += 1;
        else :
            if iteration not in valueByIterationMap:
                valueByIterationMap.update({iteration: [ (int(row[0])) ] });
            else:
                valueList = valueByIterationMap[iteration];
                valueList.append( int(row[0]) );
                valueByIterationMap.update({iteration: valueList});
    
    # print(valueByIterationMap);
    print('maxIteration: ', iteration);
    
    
    ## exercise 1: find elf with highest summed value and list the value
    sumValueList = {};
    for elfnumber in valueByIterationMap:
        sumValue = 0;
        for value in valueByIterationMap[elfnumber] :
            sumValue += value;
        sumValueList.update({elfnumber: sumValue});
    
    highestValue = 0;
    for elfnumber in sumValueList:
        if sumValueList[elfnumber] >= highestValue:
            highestValue = sumValueList[elfnumber];
    print('Highest summed value: ', highestValue);
    
    ## exercise 2: find the top 3 elfs with highest summed values and how much is that in total
    sumValueList = {};
    for elfnumber in valueByIterationMap:
        sumValue = 0;
        for value in valueByIterationMap[elfnumber] :
            sumValue += value;
        sumValueList.update({elfnumber: sumValue});
    
    value1 = 0;
    value2 = 0;
    value3 = 0;
    for elfnumber in sumValueList:
        if sumValueList[elfnumber] >= value1:
            value3 = value2;
            value2 = value1;
            value1 = sumValueList[elfnumber];
        elif sumValueList[elfnumber] >= value2:
            value3 = value2;
            value2 = sumValueList[elfnumber];
        elif sumValueList[elfnumber] >= value3:
            value3 = sumValueList[elfnumber];
            
    print('Top 3:')
    print('1: ', value1);
    print('2: ', value2);
    print('3: ', value3);
    print('total: ', value1 + value2 + value3);
    
        
        
        

            
        

