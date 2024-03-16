l=[2,0,1024,0,40,230,0]
m=[]

for i in l:
    if i!=0:
        m.append(i)

for i in range(len(l)):
    a=l[i]
    if l[i]==0:
        m.append(l[i])
        
print(m)
