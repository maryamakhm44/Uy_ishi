class Book:
	def __init__(self,title,author,year):
		self.title = title
		self.author = author
		self.year = year

	def __str__(self):
		return f"{self.title:15s}| {self.author} | {self.year}"

	def __eq__(self,other):
		return self.title == other.title


class Library:
	def __init__(self):
		self.books = []

	def add_book(self,book):
		self.books.append(book)
		print(f"Kitob qo'shildi: {book.title}")

	def __contains__(self,book):
		if book in self.books:
			return True
		return False

	def __getitem__(self,x):
		if x < len(self.books):
			return self.books[x]
		else:
			return "Book index out of range"

	def __str__(self):
		print("\n\t=== Library ===")
		for x in range(len(self.books)):
			print(f"{x + 1}) {self.books[x].title}")
		return f"\nJami: {len(self.books)} ta kitob"

if __name__ == "__main__":
	book1 = Book("Atomic Habits", "James Clear", 2018)
	book2 = Book("Python Basics", "Ali Karimov", 2025)
	book3 = Book("Clean Code", "Robert Martin", 2008)
	book4 = Book("Atomic Habits", "Unknown", 2026)

	library = Library()

	library.add_book(book1)
	library.add_book(book2)
	library.add_book(book3)

	print(book1 == book4)
	print(book4 in library)
	print(library[0])
	print(library)
