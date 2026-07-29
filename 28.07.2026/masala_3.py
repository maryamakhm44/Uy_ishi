import os
class Date:
	def __init__(self,d,m,y):
		self.day = d
		self.month = m
		self.year = y

	def get_day(self):
		return self.day

	def get_month(self):
		return self.month

	def get_year(self):
		return self.year

	def set_day(self,d):
		self.day = d

	def set_month(self,m):
		self.month = m

	def set_year(self,y):
		self.year = y

	def set_date(self,d,m,y):
		self.set_day(d)
		self.set_month(m)
		self.set_year(y)

if __name__ == "__main__":
	kun = int(input("Kun kiriting: "))
	oy = int(input("Oy kiriting: "))
	yil = int(input("Yil kiriting: "))

	if kun >= 1 and kun <= 31 and oy >= 1 and oy <= 12 and yil >= 1900 and yil <= 9999:
		data = Date(kun,oy,yil)
		print(f"\n\nKun:  {data.get_day()}")
		print(f"Oy:   {data.get_month()}")
		print(f"Yil:  {data.get_year()}\n\n")

		kun = int(input("Yangilangan kun: "))
		oy = int(input("Yangilangan oy: "))
		yil = int(input("Yangilangan yil: "))

		data.set_date(kun,oy,yil)

		print(f"\n\nKun:  {data.get_day()}")
		print(f"Oy:   {data.get_month()}")
		print(f"Yil:  {data.get_year()}")

	else:
		print("Sana xato kiritildi!")
