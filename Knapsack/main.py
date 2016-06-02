"""
	Knapsack problem
	Dynamic programming solution
	Time complexity: O(nW), n is # of items, W is maximum capacity
	Extra space: O(nW)
"""
def knapsack(A, target):
	dp=[0]*(target+1)
	for i in range(len(A)):
		for j in range(1, target+1):
			if j>=A[i]:
				dp[j]=max(dp[j], dp[j-A[i]]+A[i])
	return dp[-1]

if __name__ == '__main__':
	file=open('data.txt','r')
	data=[line.strip('\n').split(' ') for line in file]
	for i in range(1, len(data), 2):
		target=int(data[i][1])
		A=list(set([int(x) for x in data[i+1]]))
		A.sort()
		print knapsack(A, target)