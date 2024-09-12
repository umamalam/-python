n=int(input("enter the number"))
if (n%3==0) and (n%5==0): 
    print('number is divisible by 3 as well as 5')
elif (n%3==0) and (n%5!=0):
    print('number is divisible by only 3')
elif (n%5==0) and (n%5!=0):
    print('number is only divisible by 5')
elif (n%3!=0) and (n%5!=0):
    print('number is neither divisible by 3 nor divisible by 5')
