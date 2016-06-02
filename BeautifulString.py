from collections import defaultdict
def getMinRevise(s,pattern):
	char_index=defaultdict(list)
	for i,c in enumerate(s):
		char_index[c].append(i)
	print char_index

if __name__ == '__main__':
	s=['00010','01100','101010']
	pattern='010'
	for w in s:
		print getMinRevise(w,pattern)