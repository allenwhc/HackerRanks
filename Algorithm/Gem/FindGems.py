from collections import Counter

def findGems(rocks):
	if not rocks: return 0
	smallest=rocks[0]
	if len(smallest)==1: 
		
	el
	count=0
	return count

def main():
	file=open('rocks.txt','r')
	rocks=sorted([line.strip('\n') for line in file], key=len)
	file.close()
	print ('Number of gems: %d'%findGems(rocks))

if __name__ == '__main__':
	main()