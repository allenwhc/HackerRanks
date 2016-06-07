def canFinish(G, thieves):
	if max(thieves) > G: return False
	if sum(thieves) > 2 * G: return False
	if sum(thieves) <= G: return True
	total_sum = sum(thieves)
	dp=[True] + [False] * (10 ** 6 + 8)
	for i in range(len(thieves)):
		for j in range(total_sum, thieves[i] - 1, -1):
			if dp[j - thieves[i]]:
				dp[j] = True
	flag = False
	for i in range(total_sum - G, G + 1):
		if dp[i]:
			flag = True
			break
	if not flag: return False
	return True

if __name__ == '__main__':
	file = open('data.txt', 'r')
	data = [line.strip('\n').split() for line in file]
	file.close()
	for i in range(1, len(data), 2):
		G = int(data[i][1])
		thieves=[int(x) for x in data[i+1]]
		# print G, thieves
		print 'YES' if canFinish(G, thieves) else 'NO'