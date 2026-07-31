import os
class Person:
	def __init__(self,name,id_number):
		self.name = name
		self.id_number = id_number

	def get_name(self):
		return self.name

	def get_id(self):
		return self.id_number

	def show(self):
		return f"Person: {self.get_name()} ({self.get_id()})"


class Patient(Person):
	def __init__(self,name,id_number):
		super().__init__(name,id_number)
		self.diagnoses = []
		self.bill = 0

	def add_diagnosis(self,text):
		self.diagnoses.append(text)
		print("Diagnoz yozildi!")

	def add_charge(self,amount):
		if amount <= 0:
			return
		else:
			self.bill += amount

	def pay(self,amount):
		if amount > 0:
			if amount >= self.bill:
				self.bill = 0
			else:
				self.bill -= amount
			return True
		return False

	def get_balance(self):
		return self.bill

	def print_history(self):
		print(f"\n\tBemor: {self.name} ({self.id_number})")
		print("Tashxislar tarixi:")
		for x in range(len(self.diagnoses)):
			print(f"{x + 1}. {self.diagnoses[x]}")
		print(f"Joriy qarzdorlik: {self.get_balance()}")


class Doctor(Person):
	def __init__(self,name,id_number,specialty):
		super().__init__(name,id_number)
		self.specialty = specialty
		self.schedule = {}

	def add_slot(self,day,time):
		if len(self.schedule) == 0:
			self.schedule[day] = [time]
			return

		if day not in self.schedule.keys():
			self.schedule[day] = [time]

		if time not in self.schedule[day]:
			self.schedule[day].append(time)


	def book_slot(self,day,time):
		if day not in self.schedule.keys():
			return False

		if time not in self.schedule[day]:
			return False
		self.schedule[day].remove(time)
		return True

	def available_slots(self,day):
		res = []
		for x in self.schedule[day]:
			res.append(x)
		return res

	def show(self):
		return f"Dr. {self.name} ({self.specialty})"


if __name__ == "__main__":
	os.system("clear")
	p = Patient("Aziz","AB1234567")
	p.add_diagnosis("ORVI")
	p.add_diagnosis("Bronxit")
	p.add_diagnosis("Angina")
	p.add_charge(150000)
	p.add_charge(80000)
	print(p.get_balance())
	p.pay(100000)
	print(p.get_balance())
	p.print_history()

	d = Doctor("Gulrux","CD7654321","Cardiolog")
	d.add_slot("Mon","09:00")
	d.add_slot("Mon","09:30")
	print(d.book_slot("Mon","09:00"))
	print(d.book_slot("Mon","09:00"))
	print(d.available_slots("Mon"))
	print(d.show())
