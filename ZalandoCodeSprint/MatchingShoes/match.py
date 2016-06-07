from itertools import chain
from collections import Counter
def getPopularity(K, A):
	count=sorted(Counter(A).items(), key=lambda x: (-x[1], int(x[0])))
	return [x[0] for x in count[:K]]

if __name__ == '__main__':
	file=open('data.txt','r')
	data=[line.strip('\n').split() for line in file]
	file.close()
	K=int(data[0][0])
	M=int(data[0][1])
	A=list(chain(*data[1:]))
	for x in getPopularity(K, A):
		print x
	
