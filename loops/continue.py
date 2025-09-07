l=[10,16,17,18,19,15]
for i in range(len(l)):
    if l[i]%5==0:
        continue
    print(l[i]) 
print("---------------")
l1=[13,14,12,10,11]
for i in range(len(l1)):
    if l1[i]%5==0:
        continue
    print(l1[i]) 
print("-------------------")
i=0
while i<=5:
    if i==3:
        i=i+1
        continue
    print(i,i*i) 
    i=i+1   
print("---------------------")
l=[10,16,17,18,9,15,21,13]
for x in l:
    if x%2==0:
        continue
    if x%7==0:
        break
    print(x)
print("Bye")        
    
