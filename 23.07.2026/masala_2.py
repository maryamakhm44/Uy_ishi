def calculate_painting_time(ls)->int:
	if len(ls) == 0:
		return 0
	cnt = 2
	for x in range(1,len(ls)):
		cnt += 2
		if ls[x] != ls[x - 1]:
			cnt += 1
	return cnt

if __name__ == "__main__":
	pattern = ["Red","Blue","Red","Blue","Red"]
	print(calculate_painting_time(pattern))
