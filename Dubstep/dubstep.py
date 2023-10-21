theStr = input()
result = []
concatenated = ""
def check(theWord):
    global concatenated
    i = 0
    while i < len(theWord):
        if(i+2 < len(theWord) and theWord[i] == 'W' and theWord[i+1] == 'U' and theWord[i+2] == 'B'):
            result.append(concatenated)
            i += 2
            concatenated = ""
        else:
            concatenated += theWord[i]
            if(i == len(theWord)-1):
                result.append(concatenated)
                
        i += 1    
check(theStr)
for word in result:
    if(word):
        print(word, end=" ")


