n=1578
a=n
sums=0
count=0
while(n>0):
    n=n//10
    count=count+1
b=1
while(a>0):
    while(count>=b):
        temp=a%10
        sums=sums+(temp**count)
        a=a//10
        count=count-1
print(sums)
