def find_nearest_vowel(s)->str:
	try:
		ord(s)
	except:
		return "Faqat bitta kichik harf bo'lishi kerak"
	else:
		if ord(s) <= 122 and ord(s) >= 97:
			dc = {97: "a", 101: "e", 105: "i", 111: "o", 117: "u"}
			min = None
			for x in dc:
				n = x - ord(s)
				if min is None or min > abs(n):
					min = abs(n)
					res = dc[x]
			return res
		else:
			return "Faqat bitta kichik harf bo'lishi kerak"

if __name__ == "__main__":
	l = input("Kichik harf kiriting: ")
	print(find_nearest_vowel(l))
