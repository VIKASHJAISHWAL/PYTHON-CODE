print("Please select the operation")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter choice(1/2/3/4):"))
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if choice==1:
    print(num1,"+",num2,"=",num1+num2)
elif choice==2:
    print(num1,"-",num2,"=",num1-num2)
elif choice==3:
    print(num1,"*",num2,"=",num1*num2)
elif choice==4:
    print(num1,"/",num2,"=",num1/num2)
else:
    print("Invalid input")