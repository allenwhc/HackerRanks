def dfs(adjacent_list, weight, u, p, total, min_cut):
	for v in adjacent_list[u]:
		if v != p:
			dfs(adjacent_list, weight, v, u, total, min_cut)
			weight[u] += weight[v]
	if u != 0:
		min_cut[0] = min(min_cut[0], abs(total - 2*weight[u]))

def minCut(n, weight, edges):
	total = sum(weight)
	adjacent_list = [[] for i in range(n)]
	for u, v in edges:
		adjacent_list[u].append(v)
		adjacent_list[v].append(u)
	min_cut = [float('inf')]
	dfs(adjacent_list, weight, 0, 0, sum(weight), min_cut)
	return min_cut[0]

if __name__ == '__main__':
	file = open('data.txt', 'r')
	data = [line.strip('\n').split() for line in file]
	file.close()

	n = int(data[0][0])
	weight = [int(x) for x in data[1]]
	edges = []
	for i in range(2, len(data)):
		edges.append((int(data[i][0]) - 1, int(data[i][1]) - 1))
	print minCut(n, weight, edges)