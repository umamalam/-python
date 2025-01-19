import math
s=0
a=int(input('enter the number'))
for i in range(1,11):
    s=s+math.pow(a,2)/i
print(s)