import heapq,bisect
def segmentTree(A, seg, l, r, pos):
	if l==r:
		seg[pos]=A[l]
		return
	mid=int((l+r)/2)
	segmentTree(A, seg, l, mid, 2*pos+1)
	segmentTree(A, seg, mid+1, r, 2*pos+2)
	seg[pos]=seg[2*pos+1]+seg[2*pos+2]

def findMaxModuloSum(mod, A):
	prefix=[(A[0]%mod,0)]+[(0,0)]*(len(A)-1)
	for i in range(1, len(A)): prefix[i]=((prefix[i-1][0]+A[i])%mod,i)
	prefix.sort(key=lambda x: x[0])
	max_prefix_mod=max(prefix)[0]
	min_diff=float('inf')
	for i in range(len(prefix)-1):
		if prefix[i][1]>prefix[i+1][1] and 0<prefix[i+1][0]-prefix[i][0]<min_diff:
			min_diff=prefix[i+1][0]-prefix[i][0] 
	return max(max_prefix_mod, mod - min_diff)

if __name__ == '__main__':
	file=open('data.txt','r')
	data=[line.strip('\n').split(' ') for line in file]
	for i in range(1, len(data), 2):
		mod=int(data[i][1])
		array=[int(x) for x in data[i+1]]
		print (findMaxModuloSum(mod, array))