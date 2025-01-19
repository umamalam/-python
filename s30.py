import math
s=0
n=int(input('enter the number'))
a=int(input('enter the number'))
for i in range(1,n+1):
    s=s+math.pow(i,i)/math.pow(a,(i-1))
print(s)