a=int(input('enter the number'))
sum=0
for i in range(1,21):
    if i%2==0:
        sum=sum-a/i
    else:
        sum=sum+a/i
print(sum)

