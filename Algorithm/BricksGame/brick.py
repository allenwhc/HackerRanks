def brick(B):
	dp=[0]*(10**5+5)
	curr_sum=0
	for i in range(len(B)-1, -1, -1):
		curr_sum += B[i]
		dp[i] = curr_sum - min(dp[i + 1], dp[i + 2], dp[i + 3])
	return dp[0]


if __name__ == '__main__':
	file=open('data.txt', 'r')
	data=[line.strip('\n').split() for line in file]
	file.close()
	for i in range(2, len(data), 2):
		B=[int(x) for x in data[i]]
		print brick(B)