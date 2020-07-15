try:
 def add2(a,b): 
    c=a+b*a+b
    print (c)

      
 add2(int(input()),b=int(input()))
except TypeError :
     print("not given arguments")
except ValueError :
    print("the values must be integer type")
f=open('input.txt','r')
f.readlines()
f.close()
