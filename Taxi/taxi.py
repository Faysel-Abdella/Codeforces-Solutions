numberOfGroups = int(input())

groupsMem = list(map(int, input().split()))


i = 0
while i < len(groupsMem):
    for j in range(i+1, len(groupsMem)):
        if(groupsMem[i] + groupsMem[j] <= 4):
            