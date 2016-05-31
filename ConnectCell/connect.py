from collections import Counter
class UnionFind:
	def __init__(self, m=0, n=0):
		self.id=[i for i in range(m*n)]
		self.size=[1]*(m*n)

	def find(self, p):
		while p!=self.id[p]:
			p=self.id[p]
		return p

	def union(self, p, q):
		find_p=self.find(p)
		find_q=self.find(q)
		if find_p!=find_q:
			if self.size[find_p]>self.size[find_q]: 
				self.size[find_q]+=self.size[find_q]
				self.id[find_q]=self.id[find_p]
			else:
				self.size[find_q]+=self.size[find_p]
				self.id[find_p]=self.id[find_q]

def getMaxCells(grid):
	m,n=len(grid),len(grid[0])
	uf=UnionFind(m,n)
	for i in range(m):
		for j in range(n):
			if grid[i][j]==1:
				pos=i*n+j
				if i-1>=0 and grid[i-1][j]==1: uf.union(pos, pos-n)
				if i+1<m and grid[i+1][j]==1: uf.union(pos, pos+n)
				if j-1>=0 and grid[i][j-1]==1: uf.union(pos, pos-1)
				if j+1<n and grid[i][j+1]==1: uf.union(pos, pos+1)
				if i-1>=0 and j-1>=0 and grid[i-1][j-1]==1: uf.union(pos, pos-n-1)
				if i-1>=0 and j+1<n and grid[i-1][j+1]==1: uf.union(pos, pos-n+1)
				if i+1<m and j-1>=0 and grid[i+1][j-1]==1: uf.union(pos, pos+n-1)
				if i+1<m and j+1<n and grid[i+1][j+1]==1: uf.union(pos, pos+n+1)
	counter=Counter(uf.id)
	return max(counter.values())

if __name__ == '__main__':
	file=open('data.txt','r')
	data=[line.strip('\n').split(' ') for line in file]
	file.close()
	grid=[[int(x) for x in data[i]] for i in range(2, len(data))]
	print (getMaxCells(grid))