#write a recursive fuction to count the number og digitd
def count(n):
    if n==0:
        return 0
    else:
        temp=n//10
        return (1+count(temp))


n=int(input(""))
print(count(n))

