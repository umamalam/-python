n=int(input('enter the number'))
s=0
m=n
while n!=0:
    d=n%10
    s=s+d
    n=n//10
if m%s==0:
    print('it is a niven number')
else:
    print('it is not a niven number')