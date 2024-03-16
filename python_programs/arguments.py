def pos(a,b):
    print(a,b)
pos(10,20)
pos(b=10,a=20)

def defa(a=25,b=30):
    print(a,b)
defa()

def uns(**place):
    print(place["bplace"])
uns(bplace="rjy",cplace="bommuru")
