
n=int(input('enter any three digit number'))
m=n
r=0
while n!=0:
    d=n%10
    r=r*10+d
    n=n//10

diff=abs(m-r)
print("Reverse Number=",r)
print("Difference of Number=",diff)