def getMaxPrice(P):
	res,q,max_price=[],[],0
	for i in range(len(P)):
		if P[i][0]==1: 
			if q and q[-1][1] == P[i][2]:
				q.pop()
			q.append((P[i][1],P[i][2]))
		else:
			while q and P[i][1] - 59 > q[0][1]: q.pop(0)
			if q: 
				max_price=max([x[0] for x in q])
				res.append(max_price)
			else:
				res.append(-1)
	return res


if __name__ == '__main__':
	file=open('data.txt','r')
	data=[line.strip('\n').split() for line in file]
	file.close()
	P,Q=[],[]
	for i in range(1, len(data)):
		if data[i][0]=='1':
			P.append((1, int(data[i][1]), int(data[i][2])))
		else:
			P.append((2, int(data[i][1])))
	for x in getMaxPrice(P):
		print x