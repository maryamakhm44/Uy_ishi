class User:
	def __init__(self,name,email,address):
		self.name = name
		self.email = email
		self.address = address

	def get_name(self):
		return self.name

	def get_email(self):
		return self.email

	def get_address(self):
		return self.address

	def set_address(self,address):
		self.address = address
		print("Address o'zgartirildi")

	def show(self):
		print(f"User: {self.get_name():12s} <{self.get_email():20s}")

class Customer(User):
	def __init__(self,name,email,address,balance):
		super().__init__(name,email,address)
		self.cart = []
		self.balance = balance

	def add_to_cart(self,product,qty,price):
		if qty > 0 and price >= 0:
			self.cart.append((product,qty,price))
			print("Savatchaga yangi pozitsiya qo'shildi!")
		else:
			print("Xato ma'lumot kiritildi!")

	def clear_cart(self):
		self.cart.clear()
		print("Savatcha tozalandi")

	def get_cart_total(self):
		total = 0
		for x in self.cart:
			total += x[1] * x[2]
		return total

	def checkout(self):
		x = self.get_cart_total()
		if self.balance >= x:
			self.balance -= x
			self.clear_cart()
			return True
		return False
	def show(self):
		return f"Customer: {self.name} (balance: {self.balance} so'm)"



class Seller(User):
	def __init__(self,name,email,address,rating):
		super().__init__(name,email,address)
		self.rating = rating
		self.stock = {}

	def add_product(self,name,qty):
		if qty <= 0:
			return

		if name in self.stock.keys():
			self.stock[name] += qty
		else:
			self.stock[name] = qty

	def remove_product(self,name):
		if name in self.stock.keys():
			self.stock.pop(name)
			return True
		return False

	def update_stock(self,name,delta_qty):
		if name in self.stock.keys():
			new_qty = self.stock[name] - abs(delta_qty)
			if new_qty < 0:
				return False
			else:
				self.stock[name] = new_qty
				return True
		else:
			return False

	def get_stock(self):
		res = self.stock.copy()
		return res

	def show(self):
		items = 0
		for x in self.stock:
			items += self.stock[x]

		return f"Seller: {self.name} (rating: {self.rating}, items: {items})"


if __name__ == "__main__":
	c = Customer("Ali","ali@gamil.com","Toshkent",2000000)
	c.add_to_cart("Keyboard",1,300000)
	c.add_to_cart("Keyboard",2,150000)
	print(c.get_cart_total())
	print(c.checkout())
	print(c.show())

	s = Seller("Gulbahor","g@mail.com","Samarqand",4.8)
	s.add_product("Keyboard",10)
	s.update_stock("Keyboard",-3)
	print(s.get_stock())
	print(s.show())
