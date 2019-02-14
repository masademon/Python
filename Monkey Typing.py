def count_words(text,words):
	for word in words:
		count = 0
		if (word in text)==True:
			count += 1
		return count
