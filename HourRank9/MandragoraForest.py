def findMaxExperience(A):
	A.sort()
	res,n=0,len(A)
	p=0
	for i in range(n)[::-1]:
		p += A[i]
		res=max(res, p*(i+1))
	return res

if __name__ == '__main__':
	print findMaxExperience([3,2,2])