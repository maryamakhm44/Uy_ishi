import os
class book:
	def __init__(self,name,pg_cnt,p):
		self.name = name
		self.page_count = pg_cnt
		self.price = p

	def get_name(self):
		return self.name

	def get_page_count(self):
		return self.page_count

	def get_price(self):
		return self.price

	def increase_pages(self,increment):
		self.page_count += increment

	def reduce_price(self,factor):
		self.price = self.price - (self.price * factor // 100)

	def process_books(self):
		n = self.page_count
		n += 10
		if n > 100:
			self.price = self.price // 2

if __name__ == "__main__":
	os.system("clear")
	name = input("Kitob nomi: ")
	pg = int(input("Sahifalari soni: "))
	pr = float(input("Narxi: "))
	b = book(name,pg,pr)

	print(f"\n\nKitob nomi:        {b.get_name()}")
	print(f"Sahifalar soni:    {b.get_page_count()}")
	print(f"Asl narxi:         {b.get_price():.2f}")
	b.process_books()
	print(f"Sahifalar soni asosida yangilangan narx: {b.get_price():.2f}")

	inc = int(input("\n\nIncrement: "))
	fac = float(input("Factor: "))
	b.reduce_price(fac)
	b.increase_pages(inc)

	print(f"\n\nKitob nomi:                     {b.get_name()}")
	print(f"Narxi (yangilangan):            {b.get_price():.2f}")
	print(f"Sahifalar soni (yangilangan):   {b.get_page_count()}")

