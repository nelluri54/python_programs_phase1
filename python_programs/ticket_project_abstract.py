#create a class ticket which will be the abstract class inside that create a func bookticket
#which will be the abstract method and has nothing in it
#create a class makemytrip which will use the bookticket function from ticket class to take the
# details such as name phonenumber emailid journey date and displays a msg saying thankyou
# for book in makemytrip
#create a class irctc which uses bookticket of ticket class and same details as makemytrip
#but in the end it will give an option to user to select whether it is one way or round trip
#if the user option is round trip it again asks the user to enter the return date as well
#and then print msg thankyou for choosing irctc else it print the choosing irctc
#create a class indigo which takes all the details as irctc and just asks which mode of transport
#you want to go in train fligth bus display thank you msg
from abc import ABC,abstractmethod
class ticket(ABC):
    @abstractmethod
    def bookticket(self):
        pass
class makemytrip(ticket):
    def bookticket(self):
        self.name=input("enter your name:")
        self.phonenum=int(input("enter phone number:"))
        self.email=input("enter email:")
        self.jdate=input("enter journey date:")
        print("thankyou for choosing the  makemytrip")

class irctc(ticket):
    def bookticket(self):
        self.name=input("enter your name:")
        self.phonenum=int(input("enter phone number:"))
        self.email=input("enter email:")
        self.jdate=input("enter journey date:")
        print("1.oneway 2.roundtrip")
        while True:
            self.ch=input("enter your choice:")
            if(self.ch=="2" or self.ch=="roundtrip"):
                self.ch2=input("enter your return date:")
                print("thnkyou for choosing irctc")
                break
            elif(self.ch=="1" or self.ch=="oneway"):
                print("thankyou for choosing irctc")
                break
            else:
                print("invalid option")
class indigo(ticket):
    def bookticket(self):
        self.name=input("enter your name:")
        self.phonenum=int(input("enter phone number:"))
        self.email=input("enter email:")
        self.jdate=input("enter journey date:")
        print("1.oneway 2.roundtrip")
        while True:
            self.ch=input("enter your choice:")
            if(self.ch=="2" or self.ch=="roundtrip"):
                self.ch2=input("enter your return date:")
                print("thnkyou for choosing roundtrip")
                break
            elif(self.ch=="1" or self.ch=="oneway"):
                print("thankyou for choosing oneway")
                break
            else:
                print("invalid option")
        print("1.train 2.flight 3.bus")
        while True:
            self.mode=input("enter mode:")
            if(self.mode=="1" or self.mode=="train"):
                print("thank you for choosing indigo")
                break
            elif(self.mode=="2" or self.mode=="flight"):
                print("thank you for choosing indigo")
                break
            elif(self.mode=="3" or self.mode=="bus"):
                print("thankyou for choosing indigo")
                break
            else:
                print("invalid option")

print("our servies:")
print("1.makemytrip 2.irctc 2.indigo")
while True:
    a=input("")
    if(a=="1" or a=="makemytrip"):
        ob1=makemytrip()
        ob1.bookticket()
    elif(a=="2" or a=="irctc"):
        ob2=irctc()
        ob2.bookticket()
    elif(a=="3" or a=="indigo"):
        ob3=indigo()
        ob3.bookticket()
    else:
        print("invalid option")


        
    
