
for i in range(1,100):
    c=0
    for j in range(2,i):
        if i%j==0:
            c=c+1
    if c>=2:
        print(i,end=", ")