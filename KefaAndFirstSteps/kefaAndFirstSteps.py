n = int(input())
days = list(map(int, input().split()))
counter = 0

result = [0]

for i in range(1, len(days)):
    if(days[i] >= days[i-1]):
        counter += 1
        result.append(counter)
    else:
        counter = 0
        result.append(counter) 
        
print(max(result)+1)