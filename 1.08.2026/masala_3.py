class Text:
	def __init__(self,content):
		self.content = content

	def __str__(self):
		return f"{self}"

	def __len__(self):
		return len(self.content)

	def __add__(self,other):
		return self.content + other.content

	def __eq__(self,other):
		return self.content == other.content

if __name__ == "__main__":
	t1 = Text("Hello")
	t2 = Text(" World!")
	t3 = t1 + t2
	print(t3)
	print(len(t3))
	print(t1 == t2)
