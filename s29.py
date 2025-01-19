import math
s=0
n=int(input('enter the number'))
a=int(input('enter the number'))
for i in range(n,n+1):
    s=s+math.pow(a,i)
print(s,end=" + ")