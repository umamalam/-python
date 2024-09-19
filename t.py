def fact(n):
    if(n==0,n==1):
        return 1
    else:
        return n*fact(n-1)
    n=5
    print("fact of n:",fact(n))

n=int(input("enter the number"))
for i in range(1,11):
    print(n*i)


for i in range(1,16,2):
    print(i ,end="")


for i in range(2,16,2):
    print(i,end="")



for i in range(1,6):
    print()
    for j in range(i):
        print("*",end="")
