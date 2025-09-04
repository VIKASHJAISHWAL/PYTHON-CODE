# Program to find the nth term of an Arithmetic Progression (AP)
# Formula to find the nth term of an AP is nth=a+(n-1)*d
# where a is the first term and d is the common difference

a=int(input("Enter the first term: "))
d=int(input("Enter the common difference: "))
n=int(input("Enter the term number to find: "))
nth=a+(n-1)*d
print(nth)
# program to find the sum of geometric progresion (GP)
# Formula to find the sum of gp is sn=a(1-r^n)/(1-r)
# where a is the first term, r is the common ratio and n is the number of terms

a=int(input("Enter the first term: "))
r=int(input("Enter the common ratio: "))
n=int(input("Enter the number of terms: "))
sn=a*r**(n-1)
print(sn)