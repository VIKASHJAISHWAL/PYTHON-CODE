n=int(input("Enter n:"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()   
print("----------------------------------") 
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
print("------------------------------------")
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print() 
print("-------------------------------------")
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")    
        
    print()                
