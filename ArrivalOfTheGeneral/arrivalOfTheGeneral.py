soldiers = int(input())

soldiersHeight = list(map(int, input().split()))

maxHeight = max(soldiersHeight)

minHeight = 100;

indexOfMin = 0
indexOfMax = soldiersHeight.index(maxHeight)

for i in range(len(soldiersHeight)):
    if(soldiersHeight[i] <= minHeight):
        minHeight = soldiersHeight[i]
        indexOfMin = i
    
counter = 0
go = True


while go:
        if(soldiersHeight[-1] == minHeight and soldiersHeight[0] == maxHeight):
            go = False
            break
        if(soldiersHeight[-1] != minHeight):
            temp = minHeight
            soldiersHeight[indexOfMin] = soldiersHeight[indexOfMin+1]
            soldiersHeight[indexOfMin+1] = temp
            indexOfMin += 1
            counter += 1
            # print(soldiersHeight)
        if(soldiersHeight[-1] == minHeight and soldiersHeight[0] == maxHeight):
            break    
        if(soldiersHeight[0] != maxHeight):
               temp = maxHeight
               soldiersHeight[indexOfMax] = soldiersHeight[indexOfMax-1]
               soldiersHeight[indexOfMax-1] = temp
               indexOfMax -= 1
               counter += 1
            #    print(soldiersHeight)
 
if(soldiers <= 4):
    print(counter)
else:
    print(counter - 1)