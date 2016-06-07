def findMax(N,U):
	dp=[0]*(N+1)
	for start, end, value in U:
		dp[start]+=value
		if end<N: dp[end+1]-=value
	res,curr_sum=0,0
	for x in dp:
		curr_sum+=x
		res=max(res, curr_sum)
	return res

if __name__ == '__main__':
	file=open('data.txt','r')
	data=[line.strip('\n').split(' ') for line in file]
	file.close()
	N,K=int(data[0][0]),int(data[0][1])
	U=[(int(data[i][0]), int(data[i][1]), int(data[i][2])) for i in range(1, len(data))]
	print (findMax(N,U))