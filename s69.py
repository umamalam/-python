s=0
n=int(input("enter the range"))
for i in range(1,n+1):
    f1=1
    for j in range(1,i+1):
        f1=f1*j
    s=s+f1
print(s)