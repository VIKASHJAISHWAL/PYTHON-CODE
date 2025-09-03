# print(id(5))

# a=7
# print(id(a))

# b=a
# print(id(b))

'''''same id of different variables'''
a=10
b=10
print(id(a))
print(id(b))
c="Geeks"
d="Geeks"
print(id(c))
print(id(d))


"""Boolean """
a=10
b=10
print(a is b)
c=a
print(c is b)
c=20
print(c is b)
