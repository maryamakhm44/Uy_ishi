import os
class Course:
	def __init__(self,title,teacher):
		self.title = title
		self.teacher = teacher
		self.students = []

	def get_title(self):
		return self.title

	def get_teacher(self):
		return self.teacher

	def enroll(self,student_name):
		if student_name not in self.students:
			self.students.append(student_name)
			return True
		return False

	def drop(self,student_name):
		if student_name in self.students:
			self.students.remove(student_name)
			return True
		return False

	def show(self):
		return f"Course:   {self.get_title()} ({self.get_teacher()})"


class OnlineCourse(Course):
	def __init__(self,title,teacher,url,max_students):
		super().__init__(title,teacher)
		self.url = url
		self.max_students = max_students

	def enroll(self,student_name):
		if len(self.students) < self.max_students:
			self.students.append(student_name)
			return True
		return False

	def get_room(self):
		return f"Virtual: {self.url}"


class OfflineCourse(Course):
	def __init__(self,title,teacher,room,capacity):
		super().__init__(title,teacher)
		self.room = room
		self.capacity = capacity

	def enroll(self,student_name):
		if len(self.students) < self.capacity and student_name not in self.students:
			self.students.append(student_name)
			return True
		return False

	def get_room(self):
		return f"Room: {self.room}"


if __name__ == "__main__":
	os.system("clear")
	o = OnlineCourse("Python Basics","Guzal","https://nt.uz/py",2)
	print(o.enroll("Ali"))
	print(o.enroll("Vali"))
	print(o.enroll("Karim"))
	print(o.get_room())

	f = OfflineCourse("Algorithms","Dilshod","B-203",1)
	print(f.enroll("Soliha"))
	print(f.enroll("Nodir"))
	print(f.get_room())
	print(f.show())
