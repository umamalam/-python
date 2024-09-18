l=eval(input("enter the list"))
max=0
x=0
for i in range(len(l)):
    st=l[i]
    ls=len(st)
    if ls>max:
        max=ls
        x=i
    st=""
print(len(l[x]))
    
