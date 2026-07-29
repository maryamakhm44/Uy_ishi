class account:
	def __init__(self,id,name,b):
		self.id = id
		self.name = name
		self.balance = b

	def get_id(self):
		return self.id

	def get_name(self):
		return self.name

	def get_balance(self):
		return self.balance

	def pul_sol(amount):


	def pul_chiqar(amount):


	def pul_otkaz(another,amount):




if __name__ == "__main__":
	id = input("Akkaunt id: ")
	akk = input("Akkaunt nomi: ")
	balans = int(input("Balans: "))
	ac = account(id,akk,balans)
	print(ac.id + " / " + ac.name)

