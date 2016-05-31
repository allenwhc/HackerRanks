

"""
	Two pointer solution
	Time complexity: O(n)
	Extra space: O(1)
"""
def findMinCost(row_costs, col_costs):
	X,Y,res=1,1,0
	row_costs.sort(reverse=True)
	col_costs.sort(reverse=True)
	i,j=0,0
	while i<len(row_costs) and j<len(col_costs):
		if row_costs[i]>col_costs[j]:
			X+=1
			res+=row_costs[i]*Y
			i+=1
		else:
			Y+=1
			res+=col_costs[j]*X
			j+=1
	while i<len(row_costs):
		res+=row_costs[i]*Y
		i+=1
	while j<len(col_costs):
		res+=col_costs[j]*X
		j+=1
	return res % (10**9+7)

if __name__ == '__main__':
	file=open('data.txt','r')
	data=[line.strip('\n').split(' ') for line in file]
	file.close()
	for i in range(1, len(data), 3):
		rows=int(data[i][0])
		cols=int(data[i][1])
		row_costs=[int(i) for i in data[i+1]]
		col_costs=[int(i) for i in data[i+2]]
		print (findMinCost(row_costs,col_costs))