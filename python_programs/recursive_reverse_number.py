#write a recursive program to print the digits of a function in reverse order
def rev(n):
    if(n==0):
        return
    print(n%10)
    return rev(n//10)
n=int(input(""))
rev(n)
