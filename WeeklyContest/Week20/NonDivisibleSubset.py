
def findMaxSubset(S, k):
	if k==0: return 0
	L=[0]*k
	res=0
	for x in S:
		L[x % k] += 1
	for i in range(k // 2 +1):
		if i==0 or k==2*i:
			res+=bool(L[i])
		else:
			res+= max(L[i], L[k-i])
	return res

if __name__ == '__main__':
	k=3
	S=[1,7,2,4]
	print (findMaxSubset(S, k))