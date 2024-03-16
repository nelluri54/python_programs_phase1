#creating
l=[1,2,"abc",3,4,4]
print(l)
#access
print(l[1])
#slicing
print(l[:],l[1:4],l[:-1],l[:-1])
#loop accesing
for i in l:
    print(i)

#append
l.append("saijyothi")
print(l)
#insert
l.insert(4,"hlo")
print(l)
#multidimensional create and access
m=[11,2,["a","b"],"hlo",[1,2,3]]
print(m)
print(m[1:],m[1:4],m[2:5:-1],m[:-1])
#updating
m[2][1]="aa"
print(m)
