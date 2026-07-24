def find_nearest_vowel(s)->str:
	try:
		ord(s)
	except:
		return "Faqat bitta kichik harf bo'lishi kerak"
	else:
		if ord(s) <= 122 and ord(s) >= 97:
			res =
			return res
		else:
			return "Faqat bitta kichik harf bo'lishi kerak"


if __name__ == "__main__":
	l = input("Kichik harf kiriting: ")
	print(find_nearest_vowel(l))
