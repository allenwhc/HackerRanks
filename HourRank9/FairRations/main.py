import bisect
def find(A,K):
	idx=bisect.bisect_left(A,K)
	idx-=1 if A[idx]>K else 0
	if idx%2==0:
		mid=idx/2
		return A[mid]
	else:
		mid=idx/2
		return (A[mid]+A[mid+1])/2

if __name__ == '__main__':
	A=[-1,0,2,3,4,6,7]
	K=5
	print find(A,K)