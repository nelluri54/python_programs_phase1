def fact(n):
    if n==0:
        return 1
    return (n*fact(n-1))


def fib(n1):
    if n1==1:
        return 0
    if n1==2:
        return 1
    else:
        return fib(n1-1)+fib(n1-2)
n=int(input(""))
n1=int(input(""))
print(fact(n))
print(fib(n1))
