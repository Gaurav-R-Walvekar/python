class Arithematic:                         # Class Definatiopn
    value = 111                             #class variable
    
    def __init__(self,i,j):                       # Class constructor
        print("Inside Constructor")
        self.no1 = i                                # Class instance variable
        self.no2 = j                                # Instance variable

    def Add(self):                                      # instance method
        print(Arithematic.value)
        return self.no1 + self.no2
        
    def Sub(self):                                      # instance method
        return self.no1 - self.no2
        
def main():
    print("value is :",Arithematic.value)
    
    obj1 = Arithematic(21,11)               #  __init__(obj1,21,11)
    obj2 = Arithematic(101,51)              # __init__(obj2,101,51)
    print("value is :",obj1.value)
    ret = obj1.Add()                               # ret = Add(obj1)
    print("Addition is ",ret)
    ret = obj1.Sub()                                # ret = Sub(obj1)
    print("Substraction is ",ret)
    
    ret = obj2.Add()                               # ret = Add(obj2)
    print("Addition is ",ret)
    ret = obj2.Sub()                                # ret = Sub(obj2)
    print("Substraction is ",ret)

if __name__ == "__main__":
    main()









