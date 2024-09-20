l=eval(input("enter the list:"))
s=len(l)
if s%2!=0:
    s=s-1
for i in range(0,s,2):
    print(i,i+1)
    l[i],l[i+1]=l[i+1],l[i]
print("list after swapping:",l)    
    
    
