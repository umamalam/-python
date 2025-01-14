n=int(input('enter the number'))
s=0
p=1
while n!=0:
    d=n%10
    s=s+d
    p=p*d
    n=n//10
if s==p:
    print('it is a spy number')
else:
    print('it is not a spy number')