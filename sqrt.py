import math
while True:
    n=int(input('enter the number'))
    sq=math.sqrt(n)
    sqf=math.floor(sq)
    if sq-sqf==0:
        print('number is a perfect square')
    else:
        print ('number is not a perfect square')
    if n==0:
        print('program terminates')
