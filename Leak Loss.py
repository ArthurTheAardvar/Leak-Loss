import sys #needed for readline function

cases = int(sys.stdin.readline().rstrip()) #get the first number of cases

for i in range(cases): #go through the other lines
    
    line = sys.stdin.readline().rstrip()#strips off extra spaces at the end of the line
    line = line.split(" ") #split up the line by spaces
    

    Total = (float(line[0]) / (float(line[1]) - float(line[2]))) * float(line[2])

    print(float(Total))
    
    
    
    
    