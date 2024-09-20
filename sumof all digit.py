s=input("enter a string:")
sum=0
digit=""
for i in s:
    if i.isdigit():
        sum=sum+int(i)
        digit=digit+i

if sum==0:
    print(s,"has no digit")
else:
    print("original string:",s)
    print("digit are",digit)
    print("sum of all digit:",sum)
        
