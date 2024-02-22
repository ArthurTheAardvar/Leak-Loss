cases = int(input()) 

for i in range(cases): 
    
    line = input.rstrip()
    line = line().split(" ") 
    
    Total = (float(line[0]) / (float(line[1]) - float(line[2]))) * float(line[2])

    Total1 = int(Total)

    print(round(Total1))
    
    
    
    
    