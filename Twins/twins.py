coinsNo = int(input())
storeArr = list(map(int, input().split()))

counter = 0
    
storeArr.sort(reverse=True)    
sumOfCoins = sum(storeArr)
temp = 0

for coin in storeArr:
    temp += coin
    if(temp > sumOfCoins - temp):
        counter+=1
        sumOfCoins-=coin
        print(counter)
        break
    else:
        counter+=1
                   

