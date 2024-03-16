def sumf(n):
    if n==0:
        return 0
    return n%10+sumf(n//10)
print(sumf(1234))
