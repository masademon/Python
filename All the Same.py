def all_the_same(list):
	if list ==[]:
		return True
	elif list.count(list[0]) == len(list):
		return True
	else:
		return False


