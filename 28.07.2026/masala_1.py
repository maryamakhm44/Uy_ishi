import os
class account:
	def __init__(self,id,name,b = 0):
		self.id = id
		self.name = name
		self.balance = b

	def get_id(self):
		return self.id

	def get_name(self):
		return self.name

	def get_balance(self):
		return self.balance

	def pul_sol(self,amount):
		self.balance += amount
		return self.balance

	def pul_chiqar(self,amount):
		if self.balance >= amount:
			self.balance -= amount
		else:
			print("Balans yetarli emas!")
		return self.balance

	def pul_otkaz(self,another,amount):
		if self.balance >= amount:
			self.balance -= amount
			another.balance += amount
		else:
			print("Balans yetarli emas!")
		return self.balance


if __name__ == "__main__":
	os.system("clear")

	id1 = input("Akkaunt id: ")
	akk1 = input("Akkaunt nomi: ")
	balans1 = int(input("Balans: "))
	acc1 = account(id1,akk1,balans1)
	print("Account1 added")

	id2 = input("\n\nAkkaunt id: ")
	akk2 = input("Akkaunt nomi: ")
	balans2 = int(input("Balans: "))
	acc2 = account(id2,akk2,balans2)
	print("Account2 added")

	os.system("clear")

	print("--- Account 1 ---")
	print(f"ID:       {acc1.get_id()}")
	print(f"Name:     {acc1.get_name()}")
	print(f"Balans:   {acc1.get_balance()}")

	print("\n\n--- Account 2 ---")
	print(f"ID:       {acc2.get_id()}")
	print(f"Name:     {acc2.get_name()}")
	print(f"Balans:   {acc2.get_balance()}")

	sol = int(input("\n\nQo'shiladigan summa: "))
	chiq = int(input("Yechiladigan summa: "))

	print(f"\nYangi balans (acc1):  {acc1.pul_sol(sol)}")
	print(f"Yangi balans (acc2):  {acc2.pul_chiqar(chiq)}")

	amount = int(input("\n2-accountga o'tkaziladigan summa: "))
	acc1.pul_otkaz(acc2,amount)

	print("\n\n--- Total ---")
	print(f"1-account balansi:  {acc1.get_balance()}")
	print(f"2-account balansi:  {acc2.get_balance()}")
