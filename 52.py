
for i in range(10,101):
    s=0
    for j in range(1,i):
        if i%j==0:
            s=s+j
    if s>i:
        print(i,'is an abundant number')
    else:
        print(i,'is not an abundant number')
