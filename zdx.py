add=input("enter the address:")
i=0
len=len(add)
while i<len:
    ch=add[i]
    if ch.isdigit():
        sub=add[i:(i+6)]
        if sub.isdigit():
          print(sub)
          break
    i=i+1
    
    
