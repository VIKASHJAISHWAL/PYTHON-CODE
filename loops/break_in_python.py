n=int(input("Enter the n:"))
for x in range(2,n+1):
    if n%x==0:
        print(x)
        break
print("------------------------")
i=1    
while i<=5:
    if i==3:
        break
    print(i)
    i=i+1
print(i)    