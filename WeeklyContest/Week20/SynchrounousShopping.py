if __name__ == '__main__':
	file=open('divide.txt','r')
	data=[line.strip('\n').split(' ') for line in file]
	num_of_shopping_centers=int(data[0][0])
	num_of_roads=int(data[0][1])
	types_of_fish=int(data[0][2])
	fish_by_city,distance=[],{}
	for i in range(1, num_of_shopping_centers+1):
		print (data[i])
		fish_by_city.append([int(data[i][j]) for j in range(1, len(data[i]))])
	for i in range(num_of_shopping_centers+1, num_of_shopping_centers+num_of_roads+1):
		distance[(int(data[i][0]),int(data[i][1]))]=int(data[i][2])

	print  (fish_by_city, distance)