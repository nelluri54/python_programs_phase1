#prime9
num = int(input(""))

for i in range(2,int(num/2)):
    if (num % i) == 0:
        print("is not a prime number")
        break
else:
    print("is a prime number")
          
