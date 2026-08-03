class Payment:
	def __init__(self,amount):
		self.amount = amount

	def __str__(self):
		return f"To'lov: {self.payment}"

	def __add__(self,other):
		return self.amount + other.amount

	def __ge__(self,other):
		return self.amount >= other.amount

	def __le__(self,other):
		return self.amount <= other.amount

if __name__ == "__main__":
	p1 = Payment(1200)
	p2 = Payment(800)
	p3 = p1 + p2

	print(p3)
	print(p1 >= p2)
	print(p2 <= p1)
