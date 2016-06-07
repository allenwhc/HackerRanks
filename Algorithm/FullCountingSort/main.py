from collections import defaultdict
import heapq
def countingSort(A):
	pos=defaultdict(list)
	for i, x in enumerate(A):
		heapq.heappush(pos[x], i)
	n=len(A)
	B=[float('inf')]*n
	count=[0]*n
	for i in range(n): count[A[i][0]]+=1
	count=[x for x in count if x!=0]
	for i in range(1, len(count)): count[i]+=count[i-1]
	for i in range(n)[::-1]:
		B[count[A[i][0]]-1]=A[i]
		count[A[i][0]]-=1
	res=''
	for x in B:
		idx=heapq.heappop(pos[x])
		if idx<len(B)/2: res+='- '
		else: res+=x[1]+' '
	return res


if __name__ == '__main__':
	file=open('data.txt','r')
	data=[line.strip('\n').split() for line in file][1:]
	file.close()
	A=[(int(x[0]), x[1]) for x in data]
	print countingSort(A)