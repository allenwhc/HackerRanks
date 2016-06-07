
def swapPermutation(n, k):
	pass

if __name__ == '__main__':
	file=open('data.txt', 'r')
	data=[line.strip('\n').split() for line in file]
	n,k=int(data[0][0]), int (data[0][1])
	print swapPermutation(n, k)