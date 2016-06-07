
# @param n: int -> # of vertices in graph
# @param edges: List[int] -> edge connectivity
# @param pos: int -> starting vertex
# @param weight: int -> weight along every vertex
# @return: List[int] -> shortest distance from starting position to all other vertices
def bfs(adjacent_list, u, distance, res):
	pass

def shortestReach(n, edges, pos, weight):
	res=[-1]*n
	res[pos]=0
	adjacent_list=[[] for i in range(n)]
	for e in edges:
		adjacent_list[e[0]-1].append(e[1]-1)
		adjacent_list[e[1]-1].append(e[0]-1)
	q=[pos]
	while q:
		u=q.pop(0)
		for v in adjacent_list[u]:
			if res[v]==-1:
				res[v]=res[u]+1
				q.append(v)
	return [x*6 if x!=-1 else -1 for x in res if x!=0]

if __name__ == '__main__':
	file=open('data.txt','r')
	data=[line.strip('\n').split(' ') for line in file]
	file.close()
	i=1
	while i<len(data):
		num_vertices=int(data[i][0])
		num_edges=int(data[i][1])
		edges=[[int(x) for x in data[j]] for j in range(i+1, i+num_edges+1)]
		i+=num_edges+1
		start_position=int(data[i][0])
		distance=shortestReach(num_vertices, edges, start_position-1, 6)
		for d in distance:
			print d,
		print 
		i+=1