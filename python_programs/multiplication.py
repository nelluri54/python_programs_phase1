n=12345
mul=1
while(n>0):
    temp=n%10
    mul=mul*temp
    n=n//10
print(mul)
