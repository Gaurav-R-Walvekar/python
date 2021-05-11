#inheritance:Multi level inheritance
class Base:             #parant class
    def __init__(self):
        self.i=10
        self.j=20
        print("Inside Base constructor")
    
class Derived1(Base):        #child class:can access parant calss 
    def __init__(self):
        Base.__init__(self)
        self.x=30
        self.y=40
        print("Inside Derived1 constructor")
        
class Derived2(Derived1):
    def __init__(self):
        Derived1.__init__(self)
        self.a=50
        self.b=60
        print("Inside Derived2 constructor")

def main():
    dobj=Derived2()
    print(dobj.i)
    print(dobj.j)
    print(dobj.x)
    print(dobj.y)
    print(dobj.a)
    print(dobj.b)
    
if __name__=="__main__":
    main()
