#input 12345
#output 54321
n=12345
count=0
while(n>0):
    n=n//10
    count=count+1
print(count)