class Box1:
    def __init__(self,name):
        self.name=name
    def printDetails(self):
        print("Printing name:",self.name)
class Box2(Box1):
    def __init__(self,name,roll):
        self.roll=roll
        Box1.__init__(self,name)
    def printDetails(self):
        print("Printing rollNo:",self.roll)
obj=Box2("Raj",34)
obj.printDetails()                        
 
printLeftToRightManner(head)
printRightToLeftManner(head)

