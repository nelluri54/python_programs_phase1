#write a login function which accepts the user only when username and password are same and
#a mesage login successful otherwise keep asking user to enter the creden until they are correct
class login:
    def login(self):
        while True:
            username=input("enter username:")
            password=input("enter password:")
            if(username==password):
                print("login successful")
                break
            else:
                print("enter credentials correctly")      
        
a=login()
b=a.login()


