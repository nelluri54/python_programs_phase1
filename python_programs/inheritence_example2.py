#create a class of name placements which has a function info which displays "we have".
#create a another class name department with function display  which will display the names
#of dep present in the clg
#create a class pragati with a function welcome which displays the message "welcome to pragti onboard"
#the details about dep and placements
class placements:
    def plac(self):
        print("we have 635 placements and still counting")
class department:
    def display(self):
        print("the departments present in our college")
        print("cse\nds\nit\nmech\neee\nece\ncivil\nai\nai&ml\ncs")
class pragati(department,placements):
    print("welcome to pragati")



ob2=pragati()
ob2.display()
ob2.plac()

