l=eval(input("enter the list"))
l1=[]
len=len(l)

for i in range(len):
    l1[i+1]=l[i]

l[len]=l1[0]
print(l1)
