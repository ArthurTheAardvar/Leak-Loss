import sys

cases = int(input()) #get the first number of cases

for i in range(cases): #go through the other lines
    
    line = sys.stdin.readline().rstrip()#strips off extra spaces at the end of the line
    line = line.split(" ") #split up the line by spaces
    

    Total = (int(line[0]) / (int(line[1]) - int(line[2]))) * int(line[2])

    print(round(Total))
    
    
    
    
    