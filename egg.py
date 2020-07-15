try:
	a=[1,2,3]
	print(a[2])
	b={1:2,3:4}
	#print(b.get(1))
	c=('e','y','e')
	print(c)
	del a[0]
	a.append(2)
	a.insert(0,'l')
	d={5:6,7:8}
	b.update(d)
	print(b)
	e="hi what are youdoing"
	print('hi' in e)
	print(e.replace('hi','hey'))
	print(e)
except ValueError:
	print("check values")