#inheritence
class faculty:
    def __init__(self,fname,dep,fid):
        self.fname=fname
        self.dep=dep
        self.id=fid
    def print_info(self):
        print("faculty name",self.fname,"dep:",self.dep,"id:",self.id)

class cse(faculty):
    pass
ob=faculty("sai","ds","4416")
ob1=cse("jyothi","ds","4416")
ob1.print_info()
ob.print_info()
