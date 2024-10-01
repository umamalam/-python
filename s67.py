s=0
n=int(input('enter the range'))
for i in range(1,n+1):
    f=1
    for j in range(1,i+1):
        f=f*j
    s=s+1/f
    
print(s)    
         