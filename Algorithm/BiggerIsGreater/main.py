def nextPermutation(s):
	if not s: return 'no answer'
	s=list(s)
	i=len(s)-1
	while i>0 and ord(s[i-1])>=ord(s[i]): i-=1
	if i<=0: return 'no answer' # already reach the largest permutation, no other permutations are greater than this
	j=len(s)-1
	while ord(s[j])<=ord(s[i-1]): j-=1
	s[i-1],s[j]=s[j], s[i-1]
	j=len(s)-1
	while i<j:
		s[i],s[j]=s[j],s[i]
		i+=1
		j-=1
	return ''.join(s)

if __name__ == '__main__':
	file=open('data.txt','r')
	data=[line.strip('\n') for line in file]
	file.close()
	for i in range(1, len(data)):
		print nextPermutation(data[i])