def checkio(a):
	a = a.lower()
	i = []
	c = []
	d = 0
	e = 0
	f = 0
	for b in range(97,97+26):
		for s in chr(b):
			i.append(s)
			c.append(a.count(s))

			if a.count(s)>d:
				d = a.count(s)
				f = e
				e +=1
			else:
				e +=1
			

	return i[d]



			
			




