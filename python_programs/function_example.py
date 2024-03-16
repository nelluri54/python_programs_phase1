#write a function which takes 2 parameters a,b  typecast the value of secon arg into int then mul both the arf and print thelast digit of rst
def val(a,b):
    c=int(b)
    d=a*c
    print(d%10)


val(12,"3")
