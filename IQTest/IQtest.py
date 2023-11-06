def IQTest(listOfNums):
    isEven = 0
    isOdd = 0
    for num in listOfNums:
        if num % 2 == 0:
            isEven += 1
        else:
            isOdd += 1          
    if isEven > isOdd:
        for i in range(len(listOfNums)):
            if(listOfNums[i] % 2 != 0):
                return  i + 1    
    else:
        for i in range(len(listOfNums)):
            if(listOfNums[i] % 2 == 0):
                return  i + 1          

cases  = int(input())            
nums = list(map(int, input().split(" ")))

print(IQTest(nums))