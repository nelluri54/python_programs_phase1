#print out first 10 fibanocci
a=0
b=1
sum=0
print(a,b)
for i in range(1,9):
    sum=a+b
    a=b
    b=sum
    print(sum)
