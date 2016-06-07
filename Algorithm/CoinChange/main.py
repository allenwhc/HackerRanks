def coinChange(amount, coins):
	cols=amount+1
	dp=[[1 if col==0 else 0 for col in range(cols)] for _ in range(len(coins))]
	for i in range(len(dp)):
		for j in range(len(dp[0])):
			dp[i][j]=dp[i-1][j] + (dp[i][j-coins[i]] if j>=coins[i] else 0)
	return dp[-1][-1]


if __name__ == '__main__':
	file=open('data.txt','r')
	data=[line.strip('\n').split(' ') for line in file]
	file.close()

	amount=int(data[0][0])
	coins=sorted([int(x) for x in data[1]])
	print coinChange(amount,coins)