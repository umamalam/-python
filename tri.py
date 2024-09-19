a=int(input("enter the side a="))
b=int(input("enter the side b="))
c=int(input("enter the side c"))
if (a+b>c) and (b+c>a) and (c+a>b):
    print("triangle is possible")
    if (a==b) and (b==c) and (c==a):
        print ("it is an equilateral triangle")
    elif (a==b) or (b==c) or (c==a):
        print("it is an isosceles triangle")
    elif (a!=b) and (b!=c) and (c!=a):
        print("it is an scalene triangle")
else:
    print("triangle is not possible")