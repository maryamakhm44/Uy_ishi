def find_top_three_nums(d):
	for x in d:
		if len(x) > 3:
	 		x = sorted(x)
			for i in range(x - 3):
				x.remove(x[i])
		else:
			x = tuple(sorted(x))
		print(x)

if __name__ == "__main__":
	data = [(10,20,30,11),(5,15),(40,),(7,8,50,3)]
	#print(find_top_three_nums(data))
	find_top_three_nums(data)
