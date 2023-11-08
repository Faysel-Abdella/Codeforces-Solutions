games = int(input())

uniforms = []
home = []
guest = []
counter = 0

for i in range(games):
   uniforms.extend(map(int, input().split()))

for i in range(0, len(uniforms), 2):
    home.append(uniforms[i])

for i in range(1, len(uniforms), 2):
    guest.append(uniforms[i])

for i in range(len(home)):
    for j in range(len(guest)):
        if (home[i] == guest[j]):
            counter += 1
 
print(counter)

