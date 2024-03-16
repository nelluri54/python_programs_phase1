l=[12,42,23,96,7,18,10,133]
#addition of minimum and max
min=0
max=0
for i in l:
    if i>max:
        max=i
min=max
for i in l:
    if i<min:
        min=i
a=min+max
b=max-min
print(a)
print(b)
l[7]=a
l[4]=b
print(l)
