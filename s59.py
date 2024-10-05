
for i in range(1,6):
    n=int(input("enter the number"))
    c=0
    for j in range(1,n+1,1):
        if n%j==0:
            c=c+1
    if c==2:    
        print(n,"is a prime number")
    else:
        print(n,"is not a prime number")    