class Library:
	def __init__(self,books:list):
		self.books = books

	def add_book(self,name):
		if name not in self.books:
			self.books.append(name)

	def __len__(self):
		return len(self.books)

	def __str__(self):
		return f"Kutubxonada {len(self)} ta kitob mavjud."

if __name__ == "__main__":
	lib = Library(["Python Asoslari","Sun'iy Intellekt"])
	print(len(lib))
	lib.add_book("Ma'lumotlar bazasi")
	print(len(lib))
	print(lib)
