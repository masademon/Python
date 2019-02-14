def checkio(data):
	date = data.copy()
	for x in date:
		if data.count(x) == 1:
			data.remove(x)


"""
data を複製する理由は、for文がリストの要素を消去すると取り出す位置がずれ、
値が順番に取り出されなくなるから。
ex)
data = [1,2,3,4,5]
for x in data:
	if data.count(x) == 1:
		data.remove(x)
	return data
----------------------------
[2,4]
これは1が取り出された時に、次の取り出す位置が、data[1]となるために起こる。

"""