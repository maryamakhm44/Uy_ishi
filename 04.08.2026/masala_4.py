from abc import ABC,abstractmethod
class Device(ABC):
	def __init__(self):
		self._is_on = False

	@abstractmethod
	def turn_off(self):
		pass

	def turn_on(self,name):
		print(f"{name} yoqildi!")

class SmartLamp(Device):
	def __init__(self):
		super().__init__()

	def turn_on(self):
		super().turn_on("SmartLamp")

	def turn_off(self):
		print("SmartLamp o'chirildi!")


class SmartAC(Device):
	def __init__(self):
		super().__init__()

	def turn_on(self):
		super().turn_on("SmartAC")

	def turn_off(self):
		print("SmartAC o'chirildi!")


class SmartDoorLock(Device):
	def __init__(self):
		super().__init__()

	def turn_on(self):
		super().turn_on("SmartDoorLock")

	def turn_off(self):
		print("SmartDoorLock o'chirildi!")


if __name__ == "__main__":
	lamp = SmartLamp()
	ac = SmartAC()
	lock = SmartDoorLock()

	lamp.turn_on()
	lamp.turn_off()

	ac.turn_on()
	ac.turn_off()

	lock.turn_on()
	lock.turn_off()
