#check in a given year is leap year or not
#if the year is divisible by 4 and not divisible by100 or if it is divisble by 400 then it is called the leap year

n=int(input("enter year:"))

if(n%4==0 and n%100!=0) or n%400==0:
    print("leap year")
else:
    print("not leap year")
