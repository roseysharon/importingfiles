class bestmobile:                 #include object/base class 
 'bestmobile class '              #documentation line 
 def __init__(self,name='rosey',country='india'):    #initialization method     ,instance method(self)
  self.name=name;
  self.country=country; 
 @classmethod     #decorator
 def display(cls):
  print("name and country : ")
 @staticmethod    #decorator
 def displaystatic():
  print("static")
   
bestmobile.display()
x = bestmobile()     #creating object                     
print("first user :",x.name,x.country)
y=bestmobile('subhakar','india')
print("second user : ",y.name,y.country)


print(id(x)) 





#name=input("name:"),country=input("country")