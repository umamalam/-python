import math
s=0
n=int(input('enter the number'))
a=int(input('enter the numner'))
for i in range(1,n+1):
    s=s+1/math.pow(a,i)
print(s)