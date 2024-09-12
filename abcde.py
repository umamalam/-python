s=input("enter the word")
len=len(s)
for i in range(len-1,-1,-1):
    for j in range(i+1):
        print(s[j],end="")
    print()    
