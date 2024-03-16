#calucualte the difference of sum of numbers that are dicisible by 6 and not divisible by 6 in the range of first 30 numbers
temp=0
sum=0
for i in range(1,31):
    if(i%6==0):
        temp=temp+i
    else:
        sum=sum+i
a=sum-temp
print(a)
