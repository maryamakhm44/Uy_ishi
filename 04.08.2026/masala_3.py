from abc import ABC,abstractmethod
class Employee(ABC):
	def __init__(self,name,salary):
		self._name = name
		self._base_salary = salary

	@abstractmethod
	def calculate_salary(self):
		pass


class FullTimeEmp(Employee):
	def __init__(self,name,salary):
		super().__init__(name,salary)


	def calculate_salary(self,bonus,qh):
		return self._base_salary + self._base_salary * ((qh/100) + (bonus/100))

	def __str__(self):
		res = f"\nFull time employee: {self._name}\nBase salary:        {self._base_salary:.2f}"
		return res


class PartTimeEmp(Employee):
	def __init__(self,name,salary):
		super().__init__(name,salary)


	def calculate_salary(self,working_hours,qh):
		return self._base_salary * working_hours + (qh / 100)

	def __str__(self):
		res = f"\nPart time employee: {self._name}\nBase salary:        {self._base_salary:.2f}"
		return res

if __name__ == "__main__":
	s1 = int(input("Salary for full-time emp: "))
	s2 = int(input("Salary for part-time emp: "))
	full = FullTimeEmp("Ali",s1)
	part = PartTimeEmp("Vali",s2)

	b = int(input("Bonus: "))
	qh = int(input("Qo'shimcha haq: "))
	hours = int(input("Ish soatlari(part-time):"))

	print(full)
	print(f"Salary with bonus: {full.calculate_salary(b,qh):.2f}")

	print(part)
	print(f"Total salary: {part.calculate_salary(hours,qh):.2f}")
