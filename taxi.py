tno=int(input('enter the taxi number'))
dc=int(input('enter the distance covered'))
if dc<=5:
    am=100
elif dc>5 and dc<=15:
    am=100+(dc-5)*10
elif dc>15 and dc<=25:
    am=200+(dc-15)*8
elif dc>25:
    am=280+(dc-25)*5

print('taxi number=',tno)
print('ditance covered=',dc)
print('amount=',am)