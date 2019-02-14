def checkio(num):
	keys = ["M","D","C","L","X","V","I"]
	values = [1000,500,100,50,10,5,1]
	data = zip(keys,values)
	re = []
	for i,code in enumerate(values,1):
		if num>=code:
			l,num=divmod(num,code)
			re.append(keys[i]*l)

		elif num>10 and code>num:
			if code-num==values[i+1]:
				num-=code-values[i+1]
				re.append(keys[i+1]+keys[i])

			elif code-num==values[i+2]:
				num-=code-values[i+2]
				re.append(keys[i+2]+keys[i])

		else:
			continue

	return ''.join(re)


		
'''
ローマ数字は左が引き算、右が足し算になっている。
上の位から順に表し、ローマ字を連続させる。
'''


