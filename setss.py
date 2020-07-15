#set is unordered collection of elements with no duplicates
a={1,'s',1+2j,'*'}
print("a=",a)
a.add(24)#"adding of 24",
print(a)
a.discard(24)#"discarding of 24",
print(a)
b=set([1,89,'v'])
a.update(b)#"after updating a with b=",
print(a)
#union'
print("union of a and b",a|b)   
print(a.union(b))
#intersection
print("intersection of a and b",a&b)   
print(a.intersection(b))
 #difference
print("difference of a and b",a-b)  
print(a.difference(b))
#symmetric difference

print("symmetric difference of a and b",a^b)   
