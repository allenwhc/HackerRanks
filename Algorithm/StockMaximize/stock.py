def maxProfit(prices):
	res,curr_max = 0,0
	for i in range(len(prices))[::-1]:
		curr_max = max(curr_max, prices[i])
		res += curr_max - prices[i]
	return res

if __name__ == '__main__':
	file=open('data.txt','r')
	data=[line.strip('\n').split() for line in file]
	file.close()
	for i in range(2, len(data), 2):
		print maxProfit(map(int, data[i]))