class MyDate:
	def __init__(self,day,month,year):
		self.__day = day
		self.__month = month
		self.__year = year
		self.months = ['January','February','March','April','May','June','July','August','September','October','November','December']
		self.day_in_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

	def is_leap_year(self,year):
		return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

	def is_valid_date(self,day,month,year):
		if month in self.day_in_months:
			if self.day_in_months[month] >= day:
				return True

			elif self.is_leap_year(year) and day == 29 and month == 2:
				return True

		return False

	def set_date(self,day,month,year):
		if self.is_valid_date(day,month,year):
			self.__day = day
			self.__month = month
			self.__year = year
			print("Sana o'zgartirildi!")

	def next_day(self):
		if self.day_in_months[self.__month] == self.__day or (self.is_leap_year(self.__year) and self.__day == 29):
			m = self.__month
			if m == 12:
				self.__year += 1
				self.__month = 1
				self.__day = 1
			elif m == 2 and self.__day == 28 and self.is_leap_year(self.__year):
				self.__day += 1
			else:
				self.__month += 1
				self.__day = 1
		else:
			self.__day += 1
		return self.__str__()

	def previous_day(self):
		if self.__day == 1:
			m = self.__month
			if m == 1 :
				self.__year -= 1
				self.__month = 12
				self.__day = 31
			elif m == 3:
				self.__month = 2
				if self.is_leap_year(self.__year):
					self.__day = 29
				else:
					self.__day = 28
			else:
				self.__month -= 1
				self.__day = self.day_in_months[self.__month]
		else:
			self.__day -= 1
		return self.__str__()


	def __str__(self):
		return f"{self.__day}-{self.months[self.__month - 1]} {self.__year}-yil"


	def next_month(self):
		if self.__month == 12:
			self.__month = 1
			self.__year += 1
		else:
			self.__month += 1


	def previous_month(self):
		if self.__month == 1:
			self.__month = 12
			self.__year -= 1
		else:
			self.__month -= 1
			if self.is_leap_year(self.__year) and self.__month == 2 and self.__day > 29:
				self.__day = 29

	def next_year(self):
		self.__year += 1
		if self.is_leap_year(self.__year) == False and self.__month == 2 and self.__day == 29:
			self.__day = 28

	def previous_year(self):
		self.__year -= 1
		if self.is_leap_year(self.__year) == False and self.__month == 2 and self.__day == 29:
			self.__day = 28

if __name__ == "__main__":
	date = MyDate(28, 2, 2020)
	print("Boshlang'ich sana: ", date)

	print("Is leap year 2020: ",end = "")
	print("YES" if date.is_leap_year(2020) else "NO")
	print("Is leap Year 2021: ",end = "")
	print("YES" if date.is_leap_year(2021) else "NO")

	print("29-Fevral-2020 to'g'rimi? ",end = "")
	print("YES" if date.is_valid_date(29, 2, 2020) else "NO")
	print("30-Fevral-2021 to'g'rimi? ", end = "")
	print("YES" if date.is_valid_date(30, 2, 2021) else "NO")

	print("Keyingi kun: ", date.next_day())
	print("Oldingi kun: ", date.previous_day())
	date.next_month()
	print("Keyingi oydan keyin: ", date)
	date.previous_month()
	print("Oldingi oydan keyin: ", date)
	date.next_year()
	print("Keyingi yildan keyin: ", date)
	date.previous_year()
	print("Oldingi yildan keyin: ", date)

	date.set_date(15, 6, 2023)
	print("Yangi o'rnatilgan sana: ", date)

	try:
		wrong_date = MyDate(31, 4, 2023)
	except ValueError as e:
		print("Xatolik ushlandi:", e)

	leap_date = MyDate(29, 2, 2020)
	print("Kabisa sana: ", leap_date)
	leap_date.next_year()
	print("Kabisa yildan keyingi yil: ", leap_date)
