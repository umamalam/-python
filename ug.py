y=input("enter the string= ")
len=len(y)
a=len-1
for i in range(0,len):
    print(y[i],"\t\t",y[a])
    a=a-1
