def search_by_genre(cinema,janr)->list:
	res = []
	for x in cinema:
		if x['genre'] == janr:
			res.append(x)
	return res

if __name__ == "__main__":
	cinema = [{"title": "Avatar", "genre": "Fantastika", "price": 40000},
	{"title": "Sherlock", "genre": "Detektiv", "price": 30000},
	{"title": "Oq yo'l", "genre": "Drama", "price": 25000},
	{"title": "Dune", "genre": "Fantastika", "price": 35000},
	{"title": "Interstellar", "genre": "Fantastika", "price": 45000},
	{"title": "Titanic", "genre": "Drama", "price": 28000},
	{"title": "Inception", "genre": "Fantastika", "price": 38000},
	{"title": "The Batman", "genre": "Detektiv", "price": 42000}]

	janr = input("Izlayotgan filmingiz janri: ")
	result = search_by_genre(cinema,janr)
	for x in result:
		print(x)
