import os
import math as m
class circle:
	def __init__(self,r,c):
		self.radius = r
		self.color = c

	def get_radius(self):
		return self.radius

	def get_color(self):
		return self.color

	def set_radius(self,r):
		self.radius = r

	def set_color(self,c):
		self.color = c

	def get_area(self):
		return m.pi * self.radius ** 2

	def get_circumference(self):
		return 2 * m.pi * self.radius


if __name__ == "__main__":
	os.system("clear")
	r = float(input("Radius: "))
	c = input("Rang: ")
	dr = circle(r,c)

	print(f"Radius:           {dr.get_radius()}")
	print(f"Rang:             {dr.get_color()}")
	print(f"Yuzasi:           {dr.get_area():.2f}")
	print(f"Aylana uzuligi:   {dr.get_circumference():.2f}")

	r = float(input("\n\nO'zgartirilgan radius: "))
	c = input("O'zgartirilgan rang: ")
	dr.set_radius(r)
	dr.set_color(c)

	print(f"\n\nRadius:  {dr.get_radius()}")
	print(f"Rang:    {dr.get_color()}")
	print(f"Yuzasi:           {dr.get_area():.2f}")
	print(f"Aylana uzuligi:   {dr.get_circumference():.2f}")
