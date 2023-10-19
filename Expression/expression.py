a = int(input())
b = int(input())
c = int(input())

resultList = []

resultList.append(a+(b*c))
resultList.append((a*b)+c)
resultList.append(a*(b+c))
resultList.append(a*b*c)
resultList.append((a+b)*c)
resultList.append(a+b+c)

print(max(resultList))


