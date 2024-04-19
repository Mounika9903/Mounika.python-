class Box:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
class Student:
     def __init__(self,fees):
        self.fees=fees
class Box2(Box,Student):
     def __init__(self,name,roll,marks,fees):
         self.marks=marks
         Student.__init__(self,fees)
         Box.__init__(self,name,roll)
class Box3(Box2):
     def __init__(self,sem):
         self.sem=sem
         Box2.__init__(self,"Shiv-raj",12,23,200000)
obj=Box3("2-1")
print(obj.sem)
print(obj.name)
obj2=Box2("Shiv",12,23,200000)
print(obj2.fees)
print(obj2.marks)
print(obj2.name)
print(obj2.roll)
obj3=Box2("Raj kumar",45,234,100000)
print(obj3.name)
print(obj3.roll)
print(obj3.marks)
print(obj3.fees)
                     



