a=0
b=1
c=2
print(a,b,c,sep=',',end=',')
for n in range (4,11):
    d=a+b+c
    print(d,end=',')
    a=b
    b=c
    c=d