def pairs(a,k):
	answer=0
	d={e:i for i,e in enumerate(a)}
	for e in a:
		if e+k in d: answer+=1
		if e-k in d: answer+=1
		del d[e]
	return answer

if __name__ == '__main__':
	file=open('data.txt','r')
	data=[line.strip('\n').split(' ') for line in file]
	file.close()
	K=int(data[0][1])
	A=[int(x) for x in data[1]]
	print pairs(A,K)