# 810,150,630,1200
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import os
import random

class calc(QMainWindow):
	def __init__(self):
		p = QApplication([])
		super().__init__()
		self.setGeometry(730,100,730,1300)
		self.phn = QWidget(self)
		self.phn.show()
		sys.exit(p.exec_())


if __name__ == "__main__":
	app = QApplication([])
	c = calc()
	c.show()
	sys.exit(app.exec_())
