class parent:
    def __init__(self):
        self.public_var= "public"
        self._protected_var= "protected"
        self.__private_var= "private"


    def access_from_same_class(self):
        print("Accessing from same class")
        print(self.public_var)
        print(self._protected_var)
        print(self.__private_var)

class child(parent):
    
    def access_from_subclass(self):
        print("Accessing from subclass")
        print(self.public_var)
        print(self._protected_var)
        try:
            print(self.__private_var) 
        except AttributeError:
            print("Private variable is not accessible from subclass")

class stranger:
    def access_from_outside(self, p):
    
        print("Accessing from outside the class")
        print(p.public_var)
        print(p._protected_var) 
       
        try:
             print(p.__private_var) 
        except AttributeError:
            print("Private variable is not accessible from outside the class")

a=parent()
a.access_from_same_class()

b=child()
b.access_from_subclass()

c=stranger()
c.access_from_outside(a)