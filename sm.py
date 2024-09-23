import math
n=int(input('enter the number'))
sm=n
lar=n
for i in range(1,11):
    m=int(input('enter the number'))
    if m<sm:
        sm=m
    elif m>lar:
        lar=m

print('maximum number=',lar)
print('minimum number=',sm)

