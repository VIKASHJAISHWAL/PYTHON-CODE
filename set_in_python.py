# s1={10,20,30}
# print(s1)
# s2=set([20,30,40])
# print(s2)
# s3={}
# print(type(s3))
# s4=set()
# print(type(s4))
# print(s4)



#for set interaction
# print("------------------------------------")
# s={10,20}
# s.add(30)
# print(s)
# s.update([40,50])
# print(s)
# s.update({60,70},[80,90])
# print(s)

#removal opertaion
# print("------------------------------------")
# s={10,30,20,40}
# s.discard(30)
# print(s)
# s.remove(20)
# print(s)
# s.clear()
# print(s)
# s.add(50)
# print(s)
# del s


#other operations
print("------------------------------------")
s={10,30,20,40}
print(len(s))
print(20 in s)
print(50 in s)


#operation on two set(part1)
print("-------------------------------------")
s1={2,4,6,8}
s2={3,6,9}
print(s1|s2)#union
print(s1.union(s2))#union
print(s1&s2)#intersection
print(s1.intersection(s2))#intersection
print(s1-s2)#diffrence
print(s1.difference(s2))#difference
print(s1^s2)#symmetric difference
print(s1.symmetric_difference(s2))#symmetric difference
print(s1<=s2)#subset
print(s1<s2)#proper subset
print(s1>=s2)#superset
print(s1>s2)#proper superset
print(s1==s2)#equal
print(s1!=s2)#not equal
print(s1.isdisjoint(s2))#disjoint
print(s1.issubset(s2))#subset
print(s1.issuperset(s2))#superset
print(s1.copy())#copy
print(s1)
print(s2)
print(s1.clear())#clear
print(s2.clear())#clear
