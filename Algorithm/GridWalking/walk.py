def gridWalking(N, M, x, y):
	pass

if __name__ == '__main__':
	file=open('data.txt','r')
	data=[line.strip('\n').split() for line in file]
	file.close()

	for i in range(1, len(data), 3):
		N=int(data[i][0])
		M=int(data[i][1])
		start_x,start_y=int(data[i+1][0]) - 1,int(data[i+1][1]) - 1
		print gridWalking(N, M, start_x, start_y)