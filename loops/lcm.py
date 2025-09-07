a=int(input("Enter first no:"))
b=int(input("Enter second no:"))
res=max(a,b)
while(res<=a*b):
    if(res%a==0 and res%b==0):
        break
    res=res+1
print("Lcm is:",res)    
    # comment: 
# end for
print("-------------------------------")
import math
gcd=math.gcd(a,b)
lcm=(a*b)/gcd
print("Lcm is:",lcm)