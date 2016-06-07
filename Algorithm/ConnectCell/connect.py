
def dfs(grid, m, n, i, j, visited ,curr_length):
	for I, J in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1):
		if 0 <= I < m and 0 <= J < n and not visited[I][J] and grid[I][J] == 1:
			visited[I][J] = True
			curr_length[0] += 1
			dfs(grid, m, n, I, J, visited, curr_length)


def getMaxCells(grid):
	max_length = 1
	m,n=len(grid),len(grid[0])
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				curr_length=[0]
				dfs(grid, m, n, i, j, [[False] * n for i in range(m)], curr_length)
				max_length = max(max_length, curr_length[0])
	return max_length


if __name__ == '__main__':
	file=open('data.txt','r')
	data=[line.strip('\n').split(' ') for line in file]
	file.close()
	grid=[[int(x) for x in data[i]] for i in range(2, len(data))]
	print (getMaxCells(grid))