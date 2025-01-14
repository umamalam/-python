n=int(input('enter the number'))
m=n
s=0
p=1
while n!=0:
    d=n%10
    s=s+d
    p=p*d
    n=n//10
sum=s+p
if sum==m:
    print('it is a special two digit number')
else:
    print('it is not a special two digit number')