x=int(input("Enter the x:"))
res=0
while x>0:
    x=x//10
    res=res+1
print("Count of digit is:",res)    