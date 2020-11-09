from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random 
import sys 


class Window(QMainWindow): 

	def __init__(self): 
		super().__init__() 

		self.setWindowTitle("Python ") 

		self.setGeometry(100, 100, 340, 350) 

		self.UiComponents() 

		self.show() 

		self.number = 0

	def UiComponents(self): 

		head = QLabel("Number Guessing Game", self) 

		head.setGeometry(20, 10, 300, 60) 

		font = QFont('Times', 14) 
		font.setBold(True) 
		font.setItalic(True) 
		font.setUnderline(True) 

		head.setFont(font) 

		head.setAlignment(Qt.AlignCenter) 

		color = QGraphicsColorizeEffect(self) 
		head.setGraphicsEffect(color) 

		self.info = QLabel("Welcome", self) 

		self.info.setGeometry(40, 85, 260, 60) 

		self.info.setWordWrap(True) 

		self.info.setFont(QFont('Times', 13)) 
		self.info.setAlignment(Qt.AlignCenter) 

		self.info.setStyleSheet("QLabel"
								"{"
								"border : 2px solid black;"
								"background : lightgrey;"
								"}") 

		self.spin = QSpinBox(self) 

		self.spin.setRange(1, 50) 

		self.spin.setGeometry(120, 170, 100, 60) 

		self.spin.setAlignment(Qt.AlignCenter) 
		self.spin.setFont(QFont('Times', 15)) 

		check = QPushButton("Check", self) 

		check.setGeometry(130, 235, 80, 30) 

		check.clicked.connect(self.check_action) 

		start = QPushButton("Start", self) 
		start.setGeometry(65, 280, 100, 40) 

		reset_game = QPushButton("Reset", self) 

		reset_game.setGeometry(175, 280, 100, 40) 

		start.clicked.connect(self.start_action) 
		reset_game.clicked.connect(self.reset_action) 

	def start_action(self): 

		self.info.setStyleSheet("QLabel"
								"{"
								"border : 2px solid black;"
								"background : lightgrey;"
								"}") 

		self.number = random.randint(1, 20) 

		self.info.setText("Try to guess number between 1 to 50") 


	def check_action(self): 

		user_number = self.spin.value() 

		if user_number == self.number: 

			self.info.setText("Correct Guess") 
			self.info.setStyleSheet("QLabel"
									"{"
									"border : 2px solid black;"
									"background : lightgreen;"
									"}") 

		elif user_number < self.number: 

			self.info.setText("Your number is smaller") 

		else: 

			self.info.setText("Your number is bigger") 


	def reset_action(self): 
		self.info.setStyleSheet("QLabel"
								"{"
								"border : 2px solid black;"
								"background : lightgrey;"
								"}") 

		self.info.setText("Welcome") 





App = QApplication(sys.argv) 

window = Window() 

sys.exit(App.exec()) 
