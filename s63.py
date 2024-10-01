c1=0
r=0
n=int(input('enter the number'))
for x in range(1,n+1):
    if n%x==0:
        c1=c1+1

m=n
while(m!=0):
    d=m%10
    r=r*10+d
    m=m//10

c2=0
for y in range(1,r+1):
    if r%y==0:
        c2=c2+1

if c1==2 and c2==2:
    print(n,"is twisted prime number")
else:
    print(n,"is not twisted prime number")