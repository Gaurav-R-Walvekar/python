class C:
    def LearnAndCode(self):
        print("Learning C programming")

class Cpp:
    def LearnAndCode(self):
        print("Learning C++ programming")

class Golang:
    def LearnAndCode(self):
        print("Learning Golang programming")

class Demo:
    pass
    
class programmer:
    def Coding(self,language):# self,cobj
        language.LearnAndCode()#cobj.LearnAndCode  :calling method of class C

cobj=C()
cpobj=Cpp()
gobj=Golang()
obj=programmer()
dobj=Demo()

obj.Coding(cobj)
obj.Coding(cpobj)
obj.Coding(gobj)
#obj.Coding(Demo)  error because this class dont have LearnAndCode method init.