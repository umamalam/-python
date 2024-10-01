
n=int(input('enter the number'))
m=n
while(m!=0):
    d=m%10
    f=1
    for i in range(1,d+1):
        f=f*i
    print("Factorial of Digit",d,"is",f)
    m=m//10