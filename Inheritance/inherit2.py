class dad:

    def house(self):
        print ("house")

class mom:

    def shop(self):
        print ("shop")
    
class son(dad,mom):

    def factory(self):
        print ("factory")

s= son()
s.factory()
s.house()   
s.shop()