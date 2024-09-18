c=0
lst=eval(input("enter the list"))
len=len(lst)
for i in range(0,len):
    lst=[i]+1
    [i]+1=[i]+2
print(lst)    
