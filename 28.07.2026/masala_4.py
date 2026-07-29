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

	def get_first_name(self):
		return self.last_name

	def get_full_name(self):
		return f"{self.first_name} {self.last_name}"

	def get_salary(self):
		return self.salary

	def set_salary(self,s):
		self.salary = s

	def raise_salary(self,percent):
		return (self.salary * percent //100) + self.salary

	def get_annual_salary(self):
		return salary * 12

if __name__ == "__main__":

