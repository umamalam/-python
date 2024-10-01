s=0
n=int(input('enter the range'))
for i in range(1,n+1):
    s1=0
    for j in range(1,i+1):
        s1=s1+j
    s=s+s1
print(s)