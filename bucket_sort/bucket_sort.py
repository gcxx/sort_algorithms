if __name__ == '__main__':
	data_in=[4,3,3,2,6,5,1,9]
	container=[0,0,0,0,0,0,0,0,0,0,0]

	for d in data_in:
		container[d]+=1
	print container
	con=container
	output=[]
	for i in range(len(container)):
		for num in range(container[i]):
			print i

	