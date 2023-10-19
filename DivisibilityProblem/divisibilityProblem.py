cases = int(input())

for i in range(cases):
    a, b = map(int, input().split())
    counter = (b-(a%b)) % b
    print(counter)