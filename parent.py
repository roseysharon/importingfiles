class Parent():
    'declares about the properties of parent'    #documentation line
    def __init__(self,c,h):       #instance method
        self.car=c
        self.house=h

        
    def displayparentproperties(self):         #instance method
        print("parent car : ",self.car)
        print("parent house : ",self.house)

        
         
    @classmethod                #class method
    def display(cls):
        print("Family properties :")
