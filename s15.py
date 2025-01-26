import math
m=int(input("enter the number "))
n=int(input("enter the number "))
for i in range(m,n+1):
    sq=math.sqrt(i)
    if sq-math.floor(sq)==0:
        print(i)
