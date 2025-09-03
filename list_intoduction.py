l=[10,20,30,40,50]
print(l)
print(l[3])
print(l[-1])
print(l[-2])


'''''insert and search functions'''
print("-------------------------------------")
l=[10,20,30,40,50]
print(l)
l.append(30)
print(l)
l.insert(1,15)
print(l)
print(15 in l)
print(l.count(30))
print(l.index(30))
l.remove(30)
print(l)

''''removal of items'''
print("------------------------------------")
l=[10,20,30,40,50,60,70,80]
print(l)
l.remove(20)
print(l)
print(l.pop())
print(l)
print(l.pop(2))
print(l)
del l[1]
print(l)
del l[0:2]
print(l)

''''Some general purpose functions'''
print("-----------------------------------")
l=[10,40,20,50]
print(max(l))
print(min(l))
print(sum(l))
l.reverse()
print(l)
l.sort()
print(l)

print("-----------------------------------")
l=['apple', 'banana', 'cherry', 'date']
print(max(l))
print(min(l))
# print(sum(l))
l.reverse()
print(l)
l.sort()#lecture graphical order
print(l)