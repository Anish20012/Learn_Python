
from Learn_Python.Inheritance.override_parent import dad

class son(dad):

    def factory(self):
        print ("white")
    
    def house(self):
        print ("blue")

s=son()
s.factory()
s.house() 