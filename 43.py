n=int(input('enter the number'))
m=n
s=0
while n!=0:
    d=n%10
    s=s+10*d
    n=n//10
if s==m:
    print('it is a palindrome number')
else:
    print ("it is not a palindrome number")

