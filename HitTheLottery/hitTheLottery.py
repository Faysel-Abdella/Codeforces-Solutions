money = int(input())

bills = [1,5,10,20,100]

i = len(bills) - 1
counter = 0
while money != 0:
   if money % bills[i] != money:
       counter += money // bills[i] 
       money = money % bills[i]
   else:
      i -= 1       

print(counter)    





