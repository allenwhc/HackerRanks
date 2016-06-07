def commonChild(P, Q):
	m,n=len(P),len(Q)
	dp=[[0]*(5001) for i in range(5001)]
	for i in range(m):
		for j in range(n):
			if P[i] == Q[j]:
				dp[i + 1][j + 1]=dp[i][j] + 1
			else:
				dp[i + 1][j + 1]=max(dp[i + 1][j], dp[i][j + 1])
	return dp[m][n]

if __name__ == '__main__':
	file=open('data.txt','r')
	data=[line.strip('\n').split() for line in file]
	file.close()
	P,Q=data[0][0],data[1][0]
	print commonChild(P, Q)