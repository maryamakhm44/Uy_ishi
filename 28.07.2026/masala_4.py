import os
class employee:
	def __init__(self,id,fname,lname,s):
		self.id = id
		self.first_name = fname
		self.last_name = lname
		self.salary = s

	def get_id(self):
		return self.id

	def get_first_name(self):
		return self.first_name

	def get_last_name(self):
		return self.last_name

	def get_full_name(self):
		return f"{self.first_name} {self.last_name}"

	def get_salary(self):
		return self.salary

	def set_salary(self,s):
		self.salary = s

	def raise_salary(self,percent):
		if self.salary == 0:
			return "Oylik belgilanmagan"
		else:
			return (self.salary * abs(percent) //100) + self.salary

	def get_annual_salary(self):
		return self.salary * 12


if __name__ == "__main__":
	os.system("clear")
	res = []
	id = int(input("Xodim id: "))
	name = input("Nomi: ")
	fam = input("Familiyasi: ")
	sl = int(input("Oylik maoshi: "))
	emp = employee(id,name,fam,sl)

	print(f"\n\nId:             {emp.get_id()}")
	print(f"First name:     {emp.get_first_name()}")
	print(f"Last name:      {emp.get_last_name()}")
	print(f"Salary:         {emp.get_salary()}")
	print(f"Annual salary:  {emp.get_annual_salary()}")

	sl = int(input("\n\nO'zgartirilgan oylik: "))
	emp.set_salary(sl)

	print(f"\n\nId:             {emp.get_id()}")
	print(f"Full name:      {emp.get_full_name()}")
	print(f"Salary:         {emp.get_salary()}")
	print(f"Annual salary:  {emp.get_annual_salary()}")
