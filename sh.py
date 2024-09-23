import math
p=int(input('enter the principal'))
r=int(input('enter the rate'))
t=int(input('enter the time'))
si=(r*t*p)/100
ci=(p*math.pow((1+r/100),t))
diff=ci-si

print("the simple interest is;",si)
print('the compound interest is:',ci)
print(diff)
if p==0 and r==0 and t==0:
    print('program terminates')