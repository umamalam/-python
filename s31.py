import math
s=0
x=1
n=int(input('enter the number'))
a=int(input('enter the number'))
for i in range(1,n+1):
    s=s+math.pow(x,2)/math.pow(a,i)
    x=x+2
print(s)