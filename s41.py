import math
x=2
s=0
for i in range(1,21):
    if i%2==0:
        s=s-math.pow(x,i)
    else:
        s=s+math.pow(x,i)

print(s,end='' +'' )