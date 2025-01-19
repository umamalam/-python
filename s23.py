c=0
n=int(input('enter the number'))
while n!=0:
    d=n%10
    c=c+1
    n=n//10

print("number of digit=",c)
if c%2==0:
    print("the number contain even number of digit")
else:
    print("the number contain odd number of digit")