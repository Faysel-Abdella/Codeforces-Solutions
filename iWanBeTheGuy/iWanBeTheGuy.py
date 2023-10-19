totalLevel = int(input())

xLevel = list(map(int, input().split()))
yLevel = list(map(int, input().split()))

xAndyLevelsList = xLevel[1:] + yLevel[1:]

xAndyLevels = set(xAndyLevelsList) 

if(len(xAndyLevels) == totalLevel):
    print("I become the guy.")
else:
   print("Oh, my keyboard!")