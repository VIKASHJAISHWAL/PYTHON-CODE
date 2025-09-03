# Implicit type conversion
a=10
b=1.5
c=a+b
print("The sum is:", c)
d=True
e=a+d
print("the sum is:", e)

# Explicit type conversion
print("------------------------------")
s="135"
d=10+int(s)
f=float(d)
print(d)
print(f)
g="Geeks"
print(list(g))
print(tuple(g))
print(set(g))
print(dict.fromkeys(g, 0))

# Explicit conversion into string
print("-------------------------------")
l=["a","b","c","d"]
print(str(l))
a=10
b=11
print(str(a)+str(b))
c=10.5
print(str(c))


# list conversion
print("-------------------------------")
t=(1,2,5,4,6)
print(list(t))
s={5,6,9,8,7}
print(list(s))

# decimal to binary,octal,hexadecimal conversion
print("--------------------------------")
a=20
print(bin(a))
print(oct(a))
print(hex(a))

print("------------------------------------")
a="1001"
print(int(a,2))
b="12"
print(int(b,8))
c="A1"
print(int(c,16))


arr=(1,2,3,4,5,4)
print(bool(arr))
arr1=(1,2,3,4,5)
print(bool(arr1))




arr1 = (1, 2, 3, 4, 5, 4)
print(is_unique(arr1))  # False

arr2 = (1, 2, 3, 4, 5)
print(is_unique(arr2)) 