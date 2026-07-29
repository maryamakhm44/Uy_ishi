import os
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

	def show_all_acc_info(self,ls):
		for x in range(len(ls)):
			print(f"\t|{self.get_id():3s}|{self.get_name():20s}|{self.get_balance():15.2f}|")
			print(f"\t|-----------------------------------|")

#	def pul_sol(amount):


#	def pul_chiqar(amount):


#	def pul_otkaz(another,amount):




if __name__ == "__main__":
	os.system("clear")
	accounts = []
	n = int(input("Nechta akkaunt kiritmoqchisiz: "))
	for x in range(n):
		id = input("\nAkkaunt id: ")
		akk = input("Akkaunt nomi: ")
		balans = int(input("Balans: "))
		ac = account(id,akk,balans)
		accounts.append(ac)
		print("Account added\n")


	for i in range(len(accounts)):
		print(accounts[i].get_name())

	ac.show_all_acc_info(accounts)
