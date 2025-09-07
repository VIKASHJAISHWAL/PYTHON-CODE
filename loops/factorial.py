n=int(input("Enter a number:"))
res=1
for i in range(2,n+1):
    res=res*i
print("Factorial of",n,"is:",res)    
# Using library for printing factorial of a number
import math
# n=int(input("Enter a number:"))
res=math.factorial(n) 
print("Factorial is:",res)