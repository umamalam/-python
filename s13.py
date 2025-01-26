m=int(input("enter the number"))
n=int(input('enter the number'))
se=0
so=0
for i in range (m,n+1):
    if i%2==0:
        se=se+i
    else:
        so=so+i
        
print("Sum of Even Numbers =",se)
print("Sum of Odd Numbers =",so)