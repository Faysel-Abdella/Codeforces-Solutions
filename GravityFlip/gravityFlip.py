noOfCubesCol = int(input())

cubes = list(map(int, input().split()))

for i in range(len(cubes)-1, -1, -1):
    for j in range(i):
        if(cubes[i] < cubes[j]):
            difference = cubes[j] - cubes[i]
            cubes[i] += difference
            cubes[j] -= difference

for cube in cubes:
    print(cube, end=" ")