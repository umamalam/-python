y=int(input('enter the year'))
if y%4==0 and y%100!=0:
    print('year is leap year')
elif y%4==0 and y%100==0:
    print('year is century leap year')
elif y%100==0 and y%4!=0:
    print('year is  a century year but not a leap year')

    