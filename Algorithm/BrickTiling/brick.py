def getNumBrickTilling(grid):
	m,n=len(grid),len(grid[0])
	if m<=1 or n<=1: return 0
	if not any('.' in row for row in grid): return 1
	

def main():
	file=open('grids.txt','r')
	data=[line.strip('\n').split(' ') for line in file]
	file.close()
	i,grids=1,[]
	while i<len(data):
		grid=[]
		cols=int(data[i][0])
		for j in range(1, cols+1):
			grid.append(list(data[i+j][0]))
		print (grid)
		print (getNumBrickTilling(grid))
		i+=cols+1
	print (0 % 1000000007)
	

if __name__ == '__main__':
	main()