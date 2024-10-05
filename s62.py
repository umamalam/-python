s=0

n=int(input("enter the range"))
for i in range(2,n+1):
    p=1
    s1=0
    for j in range(1,i+1):
        s=s+(s1+j)/(p*j)

print(s)