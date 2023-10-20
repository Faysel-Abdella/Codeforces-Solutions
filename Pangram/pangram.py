def isPangram(word):
    newWord = word.lower()
    wordSet = set(newWord)    
    if(len(wordSet) == 26):
        print("YES")
    else:
        print("NO")


stringLen = int(input())
theString = input()

isPangram(theString)