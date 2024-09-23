num=eval(input("enter the numerators"))
denum=eval(input("enter the denominator"))
smll=num[0]/denum[0]
x=0.00
for i in range(1,len(num)):
    s=num[i]/denum[i]
    if s<smll:
        smll=s
        x=i

print("smallest fraction:",smll)
print("index of smallest fraction:",x)
        
