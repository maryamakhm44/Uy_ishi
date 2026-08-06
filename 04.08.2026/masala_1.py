from abc import ABC,abstractmethod
class Employee(ABC):
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary

	@abstractmethod
	def get_details(self):
		pass

	@abstractmethod
	def calculate_bonus(self):
		pass

class Manager(Employee):
	def __init__(self,name,salary,department):
		super().__init__(name,salary)
		self.department = department

	def get_details(self):
		print(f"""\nManager:     {self.name}\nSalary:      ${self.salary}\nDepartment:  {self.department}""")

	def calculate_bonus(self):
		return self.salary * 0.1

class Developer(Employee):
	def __init__(self,name,salary,pl):
		super().__init__(name,salary)
		self.programming_language = pl

	def get_details(self):
		print(f"""\nDeveloper:   {self.name}\nSalary:      ${self.salary}\nProgramming language: {self.programming_language}""")

	def calculate_bonus(self):
		return self.salary * 0.05

if __name__ == "__main__":
	manager = Manager("Alice",1200,"Sales")
	developer = Developer("Bob",1000,"Python")

	manager.get_details()
	developer.get_details()

	print(f"\nBonus (manager):     ${manager.calculate_bonus():.1f}")
	print(f"Bonus (developer):   ${developer.calculate_bonus():.1f}")
