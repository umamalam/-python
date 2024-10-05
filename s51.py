for i in range(1,11):
    n=int(input("enter the number = "))
    for x in range(1,n):
        if n%x==0:
            print("Factor of",n,"is",x)
    print()