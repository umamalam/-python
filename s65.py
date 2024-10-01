import math
n=int(input('enter the number'))
m=n
c=1
while(n!=0):
    d=n%10
    x=math.pow(d,c)
    print(d,"\t\t",x)
    c=c+1
    n=n//10