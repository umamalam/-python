s=input("enter the string")
len=len(s)
s1=""
for i in range(len):
    if s[i] in "aeiou" or s[i] in "AEIOU":
        s1=s1+"*"
    else:
        s1=s1+s[i]
print(s1)
