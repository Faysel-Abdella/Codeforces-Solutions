def Candies(n):
    if n == 2:
        return 0
    if n % 2 == 0:
        half = n/2
        return half - 1
    else:
        last = n - 1
        half = last/2
        return half 

tests = int(input())    
for i in range(tests):
    c = int(input())
    print(int(Candies(c)))