c=open('inpu.txt','w',+1)
txt="""hello
i am rosey.
how r u?"""
e=c.write(txt)
c.close()

d=open('input.txt','r',-1)
rd=d.readlines()
print(rd)              #gives list
for rdlinebyline in rd:
 print(rdlinebyline)
d.close()

f=open('inpu.txt','a',-1)
g=f.write('12345')
f.close()