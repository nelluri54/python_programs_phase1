class arith:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)

obj=arith()
#obj.add(10)
obj.add(1,2,3)
#python does not support function overloading
#compile polymorphism
