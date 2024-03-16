#write a program to check the onroad price of a bike under the conditions
#if the price is greater than 72000 than income tax is 10% of ur selling price insurance will be 15% actual price
#if the price is greater than 1,50,000 and less than 2,00,000 rupee the tax would be 25% insurance 20%
#if the price is above 2,00,000 then tax 35% and insurance 28%
#otherwise minimum price starts from 72000
#actual price+tax+insurance

a=int(input(""))
if (a>72000):
    if a>72000 and a<150000:
        b=a+(a*0.1)+(a*0.15)
        print(b)
    elif a>150000 and a<200000:
        b=a+(a*0.25)+(a*0.2)
        print(b)

    else:
        b=a+(a*0.35)+(a*0.28)
        print(b)
else:
    print("minimun price starts from 72000")
        
