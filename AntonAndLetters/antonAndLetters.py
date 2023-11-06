inputSet = list(input().strip("{}").split(", "))
if(inputSet[0] == ""):
    print(0)
else:
    print(len(set(inputSet)))    
