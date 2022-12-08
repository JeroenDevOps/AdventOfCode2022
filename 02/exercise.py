import csv

with open('02/data.csv',newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    
    # for row in reader:
    #     print(row)
        
    
    ## exercise 01: how many points given these rules:
    ## first column is opponent, A = Rock, B = Paper, C = Scissors
    ## second column is me, X = Rock, Y = Paper, Z = Scissor    
    ## points: win = 6, draw = 3, loss = 0   +   Rock = 1, Paper = 2, Scissors = 3
    totalPoints = 0
    for row in reader:
        match row[1]:
            case 'X':
                totalPoints += 1
                
                match row[0]:
                    case 'A':
                        totalPoints += 3
                    case 'C':
                        totalPoints += 6
            case 'Y':
                totalPoints += 2
                
                match row[0]:
                    case 'B':
                        totalPoints += 3
                    case 'A':
                        totalPoints += 6
            case 'Z':
                totalPoints += 3
                
                match row[0]:
                    case 'C':
                        totalPoints += 3
                    case 'B':
                        totalPoints += 6
       
    print(totalPoints)
    
    ## exercise 02: how many points given these rules:
    ## first column is opponent, A = Rock, B = Paper, C = Scissors
    ## second column is me, X = need to lose, Y = need to draw, Z = need to win    
    ## points: win = 6, draw = 3, loss = 0   +   Rock = 1, Paper = 2, Scissors = 3      
    
    totalPoints = 0
    condition = ''
    shape = ''
    
    
with open('02/data.csv',newline='') as csvfile:
    reader2 = csv.reader(csvfile, delimiter=' ')
    
    for row in reader2:
        if row[1] == 'X':
            condition = 'loss'
        elif row[1] == 'Y':
            condition = 'draw'
        elif row[1] == 'Z':
            condition = 'win'
        
        if row[0] == 'A':
            # rock
            if condition == 'loss':
                shape = 'scissors'
            elif condition == 'draw':
                shape = 'rock'
            elif condition == 'win':
                shape = 'paper'
        elif row[0] == 'B':
            # paper
            if condition == 'loss':
                shape = 'rock'
            elif condition == 'draw':
                shape = 'paper'
            elif condition == 'win':
                shape = 'scissors'
        elif row[0] == 'C':
            # scissors
            if condition == 'loss':
                shape = 'paper'
            elif condition == 'draw':
                shape = 'scissors'
            elif condition == 'win':
                shape = 'rock'
        
        # points:
        if condition == 'win':
            totalPoints += 6
        elif condition == 'draw':
            totalPoints += 3
        
        if shape == 'rock':
            totalPoints += 1
        elif shape == 'paper':
            totalPoints += 2
        elif shape == 'scissors':
            totalPoints += 3
    
    print(totalPoints)
    