def dfs(forest, i, j, destination, path):
	m,n=len(forest),len(forest[0])
	if i<0 or i>=m or j<0 or j>=n: return
	print i,j,forest[i][j],path
	if i==destination[0] and j==destination[1]: return
	if forest[i][j]=='X': return
	if int(i>0 and forest[i-1][j]=='.')+ \
		int(i<m-1 and forest[i+1][j]=='.')+ \
		int(j>0 and forest[i][j-1]=='.')+ \
		int(j<n-1 and forest[i][j+1]=='.')>1: path[0]+=1
	for I, J in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
		if 0<=I<m and 0<=J<n and forest[I][J]=='.':
			forest[i][j]='#'
			dfs(forest, I, J, destination, path)
			forest[i][j]='.'

def ifGetLucky(forest, guess):
	for f in forest:
		print f
	pos=[(-1,-1),(-1,-1)]
	for i in range(len(forest)):
		if 'M' in forest[i]: 
			pos[0]=(i, forest[i].index('M'))
		if '*' in forest[i]:
			pos[1]=(i, forest[i].index('*'))
		if pos[0]!=(-1,-1) and pos[1]!=(-1,-1): break
	count=[0]
	dfs(forest, pos[0][0], pos[0][1], pos[1], count)
	print guess, count[0]
	return 'Impressed' if count[0]==guess else 'Oops!'

if __name__ == '__main__':
	file=open('data.txt','r')
	data=[line.strip('\n').split(' ') for line in file]
	file.close()
	i=1
	while i<len(data):
		rows=int(data[i][0])
		cols=int(data[i][1])
		forest=[]
		for j in range(i+1, i+rows+1):
			forest.append(list(data[j][0]))
		guess=int(data[i+rows+1][0])
		print ifGetLucky(forest, guess)
		i+=rows+2