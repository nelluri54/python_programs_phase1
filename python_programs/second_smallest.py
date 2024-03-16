l=[22,-1,42,65,1,-4,6]
#write a program to find the second smallest negative number from the list
min=0
min1=l[0]
for i in range(len(l)-1):
    if(l[i]<l[i+1]):
        min=l[i]
        if(min<min1):
            min=min1
            min1=l[i]
        
        
print(min)
    
