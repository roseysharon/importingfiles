from parent import Parent

class Child(Parent):
    def __init__(self,b,c,h):
        self.bike=b
        super().__init__(c,h)

    def displaychildproperties(self):         #instance method
        print("child car : ",self.car)
        print("child house : ",self.house)
        print("child bike : ",self.house)

       
x=Child('activa','swift','rosey')
x.displaychildproperties()
x.displayparentproperties()