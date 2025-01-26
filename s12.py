cp=0
cn=0
sp=0
sn=0
for i in range(1,5):
    n=int(input ('enter the number'))
    if n>0:
        cp=cp+1
        sp=sp+n
        print("Positive Number=",n,end=", ")
    elif n<0:
        cn=cn+1
        sn=sn+n
        print('negative numbers=',n,end=", ")

print("Total Positive Numbers=",cp)
print("Total Negative Numbers=",cn)
print("sum of positive numbers=",sp)
print("sum of negative number=",sn)

