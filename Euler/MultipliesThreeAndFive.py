class ThreeFive:
	def getSumMultiplies(self, n):
		if n<3: return 0
		three,five,res=3,5,0
		while True:
			if three<n: 
				res+=three
				three+=3
			else: break
			if five<n:
				res+=five
				five+=5
				if five%3==0: res-=five
		return res
		
def main():
	n=100
	print sum([i for i in xrange(n) if i%3==0 or i%5==0])
	tf=ThreeFive()
	print tf.getSumMultiplies(n)

if __name__ == '__main__':
	main()