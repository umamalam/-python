a=int(input("enter the number a="))
b=int(input("enter the nnumber b="))
c=int(input("enter the number c="))
if a!=b and b!=c and c!=a:
    if a>b and a<c:
        print("Second Largest Number is",a)
    elif b>a and b<c:
        print("second largest number is",b)
    else:
        print("second largest number is",c)  