#write a program to check the type of triangle where u take the input from user for 3 sides
#classify accordingly into equil,isocc,scalene
a=int(input(""))
b=int(input(""))
c=int(input(""))
if(a==b and a==c):
    print("equilateral")
elif (a==b and a!=c) or (b==c and b!=c) or (a==c and a!=b):
    print("isoc")
else:
    print("scal")
