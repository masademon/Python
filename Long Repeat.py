def long_repeat(text):
    if len(text) < 1:
		return 0
	else:
		L = []
		l = list(text)
		i = 0
		re = 1
		while i < len(text)-1 :
			if l[i] == l[i+1]:
                i += 1
                re += 1
			else:
				i += 1
                re = 1
            L.append(re)
    return max(L)    
