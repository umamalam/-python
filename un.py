import math
n1=int(input('enter the number'))
n2=int(input('enter the number'))
sq1=math.sqrt(n1)
sq2=math.sqrt(n2)

d1 =sq1-math.floor(sq1)
d2 =sq2-math.floor(sq2)

if d1==0 and d2==0:
    print('both the numbers are perfect square=',d1 ,d2)
elif d1==0 and d2!=0:
    print('first number is a perfect square but second number is not a perfect square=',d1,d2)
elif d1!=0 and d2==0:
    print('second number is a perfect square=',d2)

else:
    print('neither first number nor a second number is a perfect square=',d1, d2)
