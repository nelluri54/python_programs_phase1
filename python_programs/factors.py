#take a number input from user check if the sum of factors of that number is greater than the original number or not
n=int(input(""))
a=n
temp=0
for i in range(1,int(n/2)):
    if (n%i==0):
        temp=temp+i
if(a>temp):
    print("yes")
else:
    print("no")
            
