class student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
        
    def display1(self):
            print(f"{self.name}, is in grade {self.grade}")

s1= student("Anish",10)
s2= student("Kumar",9)

s1.display1()
s2.display1() 