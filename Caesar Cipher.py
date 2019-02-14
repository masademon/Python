def to_encrypt(text,num):
    l = []
    L = list(text)
	num = int(num)
	X = []
	for c in range(97,97+26):
		X.append(chr(c))

	for i in L:
        if i == ' ':
            l.append(i)
        else:
            n = ord(i) + num -97
            if n > 26:
                n -= 26
		    i = X[n]
		    l.append(i)
	l = ''.join(l)
	return l

"""
num を26で割った余りでも可能。

""" 