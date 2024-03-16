#write a funtion to cal ssum of first n last digit of num
def sums(a):
    b=a%10
    c=a
    while(c>10):
        c=c//10
    print(b+c)

sums(1234)
