c=0
for i in range(1,6):
    n=int(input('enter the number'))
    if n%5==0:
        if n%10==5:
            print("Number Ending with 5 =",n)
        elif n%10==0:
            c=c+1
            print("Number Ending with 0 =",n)
print("Total Numbers ending with 0 =",c)