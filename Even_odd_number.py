n=int(input("Enter a number:"))
if n>0:
    print(n,"is a positive number")
    if n%2==0:
        print(n,"is a even number")
    else:
        print(n,"is a odd number")
elif n<0 :
    print(n,"is a negative number")
    if n%2==0:
        print(n,"is negative even number")
    else:
        print(n,"is negative odd number")
else:
    print("The number is zero")