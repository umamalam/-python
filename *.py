s=input("enter the string in lowercase= " )
len=len(s)
s1=""
s2=""
for i in range(0,len):
    if s[i]=="e":
        s1="*"
    else:
        s1=s[i]
    s2=s2+s1
print("New String = ",s2)
