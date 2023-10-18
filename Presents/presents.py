noOfCases = int(input())

friendNoList = list(map(int, (input().split())))

storeObj = {}


for i in range(len(friendNoList)):
    storeObj[i+1] = friendNoList[i]
    
listLen = len(friendNoList)
    
while listLen:
    mini = min(storeObj.values())
    minKey = 0
    for key, value in storeObj.items():
        if(value == mini):
            minKey = key
    print(minKey, end=" ")
    del storeObj[minKey]
    listLen -= 1