c1=0
c2=0
for i in range(1,3):
    e=int(input("enter the marks"))
    m=int(input('enter the marks of maths'))
    s=int(input('enter the marks of science'))
    agg=(e+m+s)/3
    if agg>=95:
        c1=c1+1
    if m>=90 or e>=90 or s>=90:
        c2=c2+1
    
    print("number of students who have scores 95% or more in aggregate=",c1)
    print("number of students who have scored 90% or more in english, maths and science=",c2)