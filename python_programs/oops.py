#create a class f15 with functions lights fans and ac
#lights:the color of the light which is taken as parameter to the function
#fan:the speed , taken as para of func
#ac:room temperature and the outside temperature taen as param
#display:which displays the difference inoutside and room temp of ac and alse fan speed 
class f15:
    def __init__(self,f,g):
        print("hlo,iam saijyothi")
        self.f=f
        self.g=g
        print(f,g)
    def lights(sj,a):
        print("i am ",a,"color")
    def fan(sj,b):
        sj.b=b
        print("fan is in ",b,"speed")
    def ac(sj,c,d):
        sj.e=c-d
        print("outside temperature:",c,"room temperature",d)
    def display(sj):
        print("diff:",sj.e,"speed:",sj.b)
        print(sj.f,sj.g)

obj=f15(9,4)
obj.lights("red")
obj.fan(5)
obj.ac(32,10)
obj.display()
