def find_top_three_nums(d):
	res = []
	for x in d:
		if len(x) <= 3:
			x = tuple(sorted(x,reverse = True))
		else:
			mx = []
			x = list(x)
			for _ in range(3):
				mx.append(max(x))
				x.remove(max(x))
			x = tuple(mx)
		res.append(x)
	return res

if __name__ == "__main__":
	data = [(10,20,30,11),(5,15),(40,),(7,8,50,3)]
	print(find_top_three_nums(data))
