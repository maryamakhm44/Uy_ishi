class Task:
	def __init__(self,title,subject,deadline,max_score):
		self.title = title
		self.subject = subject
		self.deadline = deadline
		self.max_score = max_score

	def __str__(self):
		res = f" {self.title:13s} | Fan: {self.subject:7s}|Deadline: {self.deadline:10s}| Ball: {self.max_score}"
		return res

class TaskManager:
	def __init__(self):
		self.tasks = []

	def add_task(self,task):
		self.tasks.append(task)
		print(f"Vazifa qo'shildi: {task.title}")

	def __len__(self):
		return len(self.tasks)

	def __getitem__(self,x):
		if x < len(self.tasks):
			return self.tasks[x]
		else:
			return "Task index out of range"
	def __str__(self):
		print("\n\t=== Task list ===")
		for x in range(len(self.tasks)):
			print(f"{x + 1}) {self.tasks[x].title}")
		return f"\nJami: {len(self.tasks)}ta vazifa"


if __name__ == "__main__":
	task1 = Task("Python OOP Project","Python","2026-05-20",100)
	task2 = Task("Database Design","SQL","2026-05-22",80)
	task3 = Task("Algorithm Challenge","DSA","2026-05-25",120)

	manager = TaskManager()

	manager.add_task(task1)
	manager.add_task(task2)
	manager.add_task(task3)

	print(manager)
	print(len(manager))
	print(manager[1])
	print(manager[4])
