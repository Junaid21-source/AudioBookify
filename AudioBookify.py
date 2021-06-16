import pyttsx3, os, webbrowser, PyPDF2, threading, pyrebase, sys
sys.dont_write_bytecode = True
from info import *
from settings import *
from file_name import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QInputDialog, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from pyttsx3.drivers import sapi5


class Ui_main_window(object):
	def setupUi(self, main_window):
		global imported_gui_mode
		path = 'Bin/Files/settings.config'
		abspath = os.path.abspath(path)
		try:
			file = open(abspath, 'r')
			imported_voice = file.readline().strip()
			imported_file_type = file.readline().strip()
			imported_quality = file.readline().strip()
			imported_gui_mode = file.readline().strip()
		except FileNotFoundError:
			msg = QMessageBox()
			msg.setWindowFlag(QtCore.Qt.FramelessWindowHint)
			msg.setIcon(QMessageBox.Critical)
			msg.setStyleSheet("QLabel{font-size: 18px;} QPushButton{ width:60px; font-size: 18px; }")
			msg.setText("Error: Please visit\nhttps:/github.com/AribMuhtasim21/AudioBookify")
			msg.setWindowTitle("Error")
			msg.exec_()
		main_window.setObjectName("main_window")
		main_window.resize(781, 511)
		main_window.setMaximumSize(QtCore.QSize(781, 511))
		main_window.setMinimumSize(QtCore.QSize(781, 511))
		main_window.setWindowFlags(main_window.windowFlags() & QtCore.Qt.CustomizeWindowHint)
		main_window.setWindowFlags(main_window.windowFlags() & ~QtCore.Qt.WindowMinMaxButtonsHint)
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(16)
		main_window.setFont(font)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("Bin/Icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		main_window.setWindowIcon(icon)
		if imported_gui_mode == 'Dark Mode':
			main_window.setStyleSheet("background-color: rgb(79, 80, 81);")
		if imported_gui_mode == 'Light Mode':
			main_window.setStyleSheet("background-color: rgb(255, 255, 255);")
		main_window.setUnifiedTitleAndToolBarOnMac(True)
		self.centralwidget = QtWidgets.QWidget(main_window)
		self.centralwidget.setObjectName("centralwidget")
		self.title_text = QtWidgets.QLabel(self.centralwidget)
		self.title_text.setGeometry(QtCore.QRect(90, 10, 601, 61))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(28)
		self.title_text.setFont(font)
		self.title_text.setObjectName("title_text")
		self.title_logo = QtWidgets.QLabel(self.centralwidget)
		self.title_logo.setGeometry(QtCore.QRect(10, 10, 71, 61))
		self.title_logo.setText("")
		self.title_logo.setPixmap(QtGui.QPixmap("Bin/Icons/logo.png"))
		self.title_logo.setScaledContents(True)
		self.title_logo.setObjectName("title_logo")
		self.right_bar = QtWidgets.QFrame(self.centralwidget)
		self.right_bar.setGeometry(QtCore.QRect(710, 0, 71, 511))
		if imported_gui_mode == 'Dark Mode':
			self.right_bar.setStyleSheet("background-color: rgb(13, 118, 222);")
		if imported_gui_mode == 'Light Mode':
			self.right_bar.setStyleSheet("background-color: rgb(82, 183, 255);")
		self.right_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.right_bar.setFrameShadow(QtWidgets.QFrame.Raised)
		self.right_bar.setObjectName("right_bar")
		self.github_link = QtWidgets.QPushButton(self.right_bar)
		self.github_link.setGeometry(QtCore.QRect(10, 10, 51, 51))
		self.github_link.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		if imported_gui_mode == 'Dark Mode':
			self.github_link.setStyleSheet("border: 0px solid rgb(139, 139, 139);")
		if imported_gui_mode == 'Light Mode':
			self.github_link.setStyleSheet("border: 0px solid rgb(255, 84, 84);")
		self.github_link.setText("")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("Bin/Icons/github-icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.github_link.setIcon(icon)
		self.github_link.setIconSize(QtCore.QSize(50, 50))
		self.github_link.setObjectName("github_link")
		self.github_link.clicked.connect(self.github_link_web)
		self.settings_btn = QtWidgets.QPushButton(self.right_bar)
		self.settings_btn.setGeometry(QtCore.QRect(10, 450, 51, 51))
		self.settings_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		if imported_gui_mode == 'Dark Mode':
			self.settings_btn.setStyleSheet("border: 0px solid rgb(139, 139, 139);")
		if imported_gui_mode == 'Light Mode':
			self.settings_btn.setStyleSheet("border: 0px solid rgb(255, 84, 84);")
		self.settings_btn.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("Bin/Icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.settings_btn.setIcon(icon1)
		self.settings_btn.setIconSize(QtCore.QSize(50, 50))
		self.settings_btn.setObjectName("settings_btn")
		self.settings_btn.clicked.connect(self.settings_opener)
		self.web_link = QtWidgets.QPushButton(self.right_bar)
		self.web_link.setGeometry(QtCore.QRect(10, 80, 51, 51))
		self.web_link.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		if imported_gui_mode == 'Dark Mode':
			self.web_link.setStyleSheet("border: 0px solid rgb(139, 139, 139);")
		if imported_gui_mode == 'Light Mode':
			self.web_link.setStyleSheet("border: 0px solid rgb(82, 183, 255);")
		self.web_link.setText("")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap("Bin/Icons/web-icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.web_link.setIcon(icon2)
		self.web_link.setIconSize(QtCore.QSize(50, 50))
		self.web_link.setObjectName("web_link")
		self.web_link.clicked.connect(self.link_web)
		self.text_option_1 = QtWidgets.QTextEdit(self.centralwidget)
		self.text_option_1.setGeometry(QtCore.QRect(10, 90, 691, 121))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(12)
		self.text_option_1.setFont(font)
		self.text_option_1.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
		self.text_option_1.setFocusPolicy(QtCore.Qt.ClickFocus)
		if imported_gui_mode == 'Dark Mode':
			self.text_option_1.setStyleSheet("border: 3px solid rgb(139, 139, 139);\n"
			"border-radius: 5px;\n"
			"color: rgb(255, 255, 255);\n"
			"background-color: rgb(79, 80, 81);")
		if imported_gui_mode == 'Light Mode':
			self.text_option_1.setStyleSheet("border: 3px solid rgb(82, 183, 255);\n"
			"border-radius: 5px;\n"
			"color: rgb(255, 255, 255);\n"
			"background-color: rgb(82, 183, 255);")
		self.text_option_1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
		self.text_option_1.setCursorWidth(3)
		self.text_option_1.setObjectName("text_option_1")
		self.text_option_2 = QtWidgets.QLineEdit(self.centralwidget)
		self.text_option_2.setGeometry(QtCore.QRect(10, 230, 581, 31))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(10)
		self.text_option_2.setFont(font)
		self.text_option_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
		if imported_gui_mode == 'Dark Mode':
			self.text_option_2.setStyleSheet("border: 3px solid rgb(139, 139, 139);\n"
			"border-radius: 5px;\n"
			"color: rgb(0, 0, 0)\n")
		if imported_gui_mode == 'Light Mode':
			self.text_option_2.setStyleSheet("border: 3px solid rgb(82, 183, 255);\n"
			"border-radius: 5px;\n"
			"color: rgb(0, 0, 0)\n")
		self.text_option_2.setReadOnly(True)
		self.text_option_2.setObjectName("text_option_2")
		self.select_file_btn = QtWidgets.QPushButton(self.centralwidget)
		self.select_file_btn.setGeometry(QtCore.QRect(600, 230, 101, 31))
		self.select_file_btn.clicked.connect(self.file_importing)
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(10)
		self.select_file_btn.setFont(font)
		self.select_file_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.select_file_btn.setStyleSheet("border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(82, 183, 255);")
		if imported_gui_mode == 'Dark Mode':
			self.select_file_btn.setStyleSheet("border-radius: 5px;\n"
			"color: rgb(60, 74, 81);\n"
			"background-color: rgb(139, 139, 139);")
		if imported_gui_mode == 'Light Mode':
			self.select_file_btn.setStyleSheet("border-radius: 5px;\n"
			"color: rgb(255, 255, 255);\n"
			"background-color: rgb(82, 183, 255);")
		self.select_file_btn.setObjectName("Bin/Icons/select_file_btn")
		self.seperator1 = QtWidgets.QFrame(self.centralwidget)
		self.seperator1.setGeometry(QtCore.QRect(10, 263, 691, 20))
		self.seperator1.setFrameShape(QtWidgets.QFrame.HLine)
		self.seperator1.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.seperator1.setObjectName("seperator1")
		self.advanced_label = QtWidgets.QLabel(self.centralwidget)
		self.advanced_label.setGeometry(QtCore.QRect(10, 280, 691, 21))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(16)
		self.advanced_label.setFont(font)
		self.advanced_label.setObjectName("advanced_label")
		self.export_btn = QtWidgets.QPushButton(self.centralwidget)
		self.export_btn.setGeometry(QtCore.QRect(650, 450, 50, 50))
		self.export_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		if imported_gui_mode == 'Dark Mode':
			self.export_btn.setStyleSheet("border-radius: 25px;\n"
		"background-color: rgb(13, 118, 222);")
		if imported_gui_mode == 'Light Mode':
			self.export_btn.setStyleSheet("border-radius: 25px;\n"
		"background-color: rgb(82, 183, 255);")
		self.export_btn.setText("")
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap("Bin/Icons/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.export_btn.setIcon(icon3)
		self.export_btn.setIconSize(QtCore.QSize(26, 26))
		self.export_btn.setObjectName("export_btn")
		self.export_btn.clicked.connect(self.file_name_opener)
		self.info_btn = QtWidgets.QPushButton(self.centralwidget)
		self.info_btn.setGeometry(QtCore.QRect(670, 10, 31, 31))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(14)
		self.info_btn.setFont(font)
		self.info_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		if imported_gui_mode == 'Dark Mode':
			self.info_btn.setStyleSheet("border-radius: 10.5px;\n"
		"background-color: rgb(13, 118, 222);")
		if imported_gui_mode == 'Light Mode':
			self.info_btn.setStyleSheet("border-radius: 10.5px;\n"
		"background-color: rgb(82, 183, 255);")
		self.info_btn.setIconSize(QtCore.QSize(15, 15))
		self.info_btn.setObjectName("info_btn")
		self.info_btn.clicked.connect(self.info_btn_work)
		self.voice_label = QtWidgets.QLabel(self.centralwidget)
		self.voice_label.setGeometry(QtCore.QRect(10, 320, 191, 21))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(12)
		self.voice_label.setFont(font)
		self.voice_label.setObjectName("voice_label")
		self.gender_selector = QtWidgets.QComboBox(self.centralwidget)
		self.gender_selector.setGeometry(QtCore.QRect(10, 350, 191, 31))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(12)
		self.gender_selector.setFont(font)
		if imported_gui_mode == 'Dark Mode':
			self.gender_selector.setStyleSheet("border: 2px solid rgb(139, 139, 139);\n"
		"color: rgb(0, 0, 0);\n")
		if imported_gui_mode == 'Light Mode':
			self.gender_selector.setStyleSheet("border: 2px solid rgb(82, 183, 255);\n"
		"color: rgb(0, 0, 0);\n")
		self.gender_selector.setIconSize(QtCore.QSize(0, 0))
		self.gender_selector.setObjectName("gender_selector")
		self.gender_selector.addItem("")
		self.gender_selector.addItem("")
		if imported_voice == 'Male Voice':
			self.gender_selector.setCurrentIndex(0)
		if imported_voice == 'Female Voice':
			self.gender_selector.setCurrentIndex(1)
		self.voice_tester = QtWidgets.QPushButton(self.centralwidget)
		self.voice_tester.setGeometry(QtCore.QRect(210, 350, 31, 31))
		self.voice_tester.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		if imported_gui_mode == 'Dark Mode':
			self.voice_tester.setStyleSheet("border: 2px solid rgb(139, 139, 139);")
		if imported_gui_mode == 'Light Mode':
			self.voice_tester.setStyleSheet("border: 2px solid rgb(82, 183, 255);")
		self.voice_tester.setText("")
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap("Bin/Icons/speaker-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.voice_tester.setIcon(icon4)
		self.voice_tester.setObjectName("voice_tester")
		self.voice_tester.clicked.connect(self.tester)
		self.file_label = QtWidgets.QLabel(self.centralwidget)
		self.file_label.setGeometry(QtCore.QRect(10, 400, 191, 21))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(12)
		self.file_label.setFont(font)
		self.file_label.setObjectName("file_label")
		self.file_selector = QtWidgets.QComboBox(self.centralwidget)
		self.file_selector.setGeometry(QtCore.QRect(10, 430, 191, 31))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(12)
		self.file_selector.setFont(font)
		if imported_gui_mode == 'Dark Mode':
			self.file_selector.setStyleSheet("border: 2px solid rgb(139, 139, 139);\n"
		"color: rgb(0, 0, 0);\n")
		if imported_gui_mode == 'Light Mode':
			self.file_selector.setStyleSheet("border: 2px solid rgb(82, 183, 255);\n"
		"color: rgb(0, 0, 0);\n")
		self.file_selector.setIconSize(QtCore.QSize(0, 0))
		self.file_selector.setObjectName("file_selector")
		self.file_selector.addItem("")
		self.file_selector.addItem("")
		self.file_selector.addItem("")
		if imported_file_type == 'MP3':
			self.file_selector.setCurrentIndex(0)
		if imported_file_type == 'WAV':
			self.file_selector.setCurrentIndex(1)
		if imported_file_type == 'OGG':
			self.file_selector.setCurrentIndex(2)
		self.quality_selector = QtWidgets.QComboBox(self.centralwidget)
		self.quality_selector.setGeometry(QtCore.QRect(10, 470, 191, 31))
		font = QtGui.QFont()
		font.setFamily("consolas")
		font.setPointSize(12)
		self.quality_selector.setFont(font)
		if imported_gui_mode == 'Dark Mode':
			self.quality_selector.setStyleSheet("border: 2px solid rgb(139, 139, 139);\n"
		"color: rgb(0, 0, 0);\n")
		if imported_gui_mode == 'Light Mode':
			self.quality_selector.setStyleSheet("border: 2px solid rgb(82, 183, 255);\n"
		"color: rgb(0, 0, 0);\n")
		self.quality_selector.setIconSize(QtCore.QSize(0, 0))
		self.quality_selector.setObjectName("quality_selector")
		self.quality_selector.addItem("")
		self.quality_selector.addItem("")
		self.quality_selector.addItem("")
		if imported_quality == 'Excellent Quality':
			self.quality_selector.setCurrentIndex(0)
		main_window.setCentralWidget(self.centralwidget)
		if imported_quality == 'Medium Quality':
			self.quality_selector.setCurrentIndex(1)
		main_window.setCentralWidget(self.centralwidget)
		if imported_quality == 'Normal Quality':
			self.quality_selector.setCurrentIndex(2)
		main_window.setCentralWidget(self.centralwidget)

		self.retranslateUi(main_window)
		QtCore.QMetaObject.connectSlotsByName(main_window)
			
	def file_importing(self):
		global opened_file, pdf_processing_ran, file_name
		pdf_processing_ran = False
		opened_file = QFileDialog.getOpenFileName(None, 'Select File', "", "PDF (*.pdf);;TXT (*.txt)")
		file_name = opened_file[0]
		self.text_option_2.setText(file_name)
		if ".pdf" in file_name:
			pdf_processing_ran = True
			self.pdf_processing()

	def pdf_processing(self):
		global extracted_pdf_text
		pdf_reader = PyPDF2.PdfFileReader(file_name)
		for i in range(pdf_reader.numPages):
			page = pdf_reader.getPage(i)
			extracted_pdf_text = page.extractText()

	def exporting_1(self):
		if self.text_option_1.toPlainText() == '':
			self.exporting_2()

		else:
			engine = pyttsx3.init()
			myText = self.text_option_1.toPlainText()
			language = "english"
			engine.setProperty('voice', language)
			rate = engine.getProperty('rate')
			engine.setProperty('rate', 125)
			file_type = self.file_selector.currentText()
			gender = self.gender_selector.currentText()
			if gender == 'Male Voice':
				voices = engine.getProperty('voices')
				engine.setProperty('voice', voices[0].id)
			if gender == 'Female Voice':
				voices = engine.getProperty('voices')
				engine.setProperty('voice', voices[1].id)
			if file_type == 'MP3':
				engine.save_to_file(myText, file_name + '.mp3')
				engine.runAndWait()
				engine.stop()
			if file_type == 'WAV':
				engine.save_to_file(myText, file_name + '.wav')
				engine.runAndWait()
				engine.stop()
			if file_type == 'OGG':
				engine.save_to_file(myText, file_name + '.ogg')
				engine.runAndWait()
				engine.stop()

	
	def exporting_2(self):
		engine = pyttsx3.init()
		rate = engine.getProperty('rate')
		engine.setProperty('rate', 125)
		try:
			if pdf_processing_ran == True:
				myText = extracted_pdf_text
				language = "english"
				engine.setProperty('voice', language)
				file_type = self.file_selector.currentText()
				gender = self.gender_selector.currentText()
				if gender == 'Male Voice':
					voices = engine.getProperty('voices')
					engine.setProperty('voice', voices[0].id)
				if gender == 'Female Voice':
					voices = engine.getProperty('voices')
					engine.setProperty('voice', voices[1].id)
				if file_type == 'MP3':
					engine.save_to_file(myText, file_name + '.mp3')
					engine.runAndWait()
					engine.stop()
					self.text_option_2.setText('')
				if file_type == 'WAV':
					engine.save_to_file(myText, file_name + '.wav')
					engine.runAndWait()
					engine.stop()
					self.text_option_2.setText('')
				if file_type == 'OGG':
					engine.save_to_file(myText, file_name + '.ogg')
					engine.runAndWait()
					engine.stop()
					self.text_option_2.setText('')
			else:
				file_ = self.text_option_2.text()
				myText = open(file_, 'rt').read()
				language = "english"
				engine.setProperty('voice', language)
				file_type = self.file_selector.currentText()
				gender = self.gender_selector.currentText()
				if gender == 'Male Voice':
					voices = engine.getProperty('voices')
					engine.setProperty('voice', voices[0].id)
				if gender == 'Female Voice':
					voices = engine.getProperty('voices')
					engine.setProperty('voice', voices[1].id)
				if file_type == 'MP3':
					engine.save_to_file(myText, file_name + '.mp3')
					engine.runAndWait()
					engine.stop()
					self.text_option_2.setText('')
				if file_type == 'WAV':
					engine.save_to_file(myText, file_name + 'wav')
					engine.runAndWait()
					engine.stop()
					self.text_option_2.setText('')
				if file_type == 'OGG':
					engine.save_to_file(myText, file_name + 'ogg')
					engine.runAndWait()
					engine.stop()
					self.text_option_2.setText('')
		except:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Critical)
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap("Bin/Icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			msg.setWindowIcon(icon)
			msg.setStyleSheet("QLabel{font-size: 18px;} QPushButton{ width:60px; font-size: 18px; }")
			msg.setText("Error: Please set the text or select a file.")
			msg.setWindowTitle("Error")
			msg.exec_()

	def tester(self):
		engine = pyttsx3.init()
		engine.setProperty('voice', 'english')
		rate = engine.getProperty('rate')
		engine.setProperty('rate', 150)
		gender = self.gender_selector.currentText()
		if gender == 'Male Voice':
			voices = engine.getProperty('voices')
			engine.setProperty('voice', voices[0].id)
		if gender == 'Female Voice':
			voices = engine.getProperty('voices')
			engine.setProperty('voice', voices[1].id)
		engine.say('Hello, This is a test')
		engine.runAndWait()
		engine.stop()

	def github_link_web(self):
		webbrowser.open("https://github.com/AribMuhtasim21/AudioBookify")
			
	def link_web(self):
		webbrowser.open('https://github.com/AribMuhtasim21/AudioBookify')
	
	def guide_opener(self):
		webbrowser.open('https://github.com/AribMuhtasim21/AudioBookify/blob/main/Readme.md')

	def info_btn_work(self):
		self.info_window = QtWidgets.QMainWindow()
		self.ui = Ui_info_window()
		self.ui.setupUi(self.info_window)
		self.info_window.show()
		self.ui.guide_button.clicked.connect(self.guide_opener)
	
	def file_name_opener(self):
		self.file_name_picker = QtWidgets.QMainWindow()
		self.ui = Ui_File_picker()
		self.ui.setupUi(self.file_name_picker)
		self.file_name_picker.show()
		self.ui.final_export_btn.clicked.connect(self.name_finalizing)
		self.ui.cancel_btn.clicked.connect(self.file_name_close)

	def name_finalizing(self):
		global file_name
		file_name = self.ui.file_name_picked.text()
		self.exporting_1()
		ui.file_name_picker.close()

	def file_name_close(self):
		ui.file_name_picker.close()

	def settings_opener(self):
		self.settings_window = QtWidgets.QMainWindow()
		self.ui = Ui_settings_window()
		self.ui.setupUi(self.settings_window)
		self.settings_window.show()
		self.ui.message_btn.clicked.connect(self.feedback_sys)
		self.ui.save_btn.clicked.connect(self.defaults_saves)
		self.ui.light_btn.clicked.connect(self.light_mode_stw)
		self.ui.dark_btn.clicked.connect(self.dark_mode_stw)
	
	def feedback_sys(self):
		feedbacker_name = "Name: " + self.ui.name_box.text()
		feedbacker_msg = self.ui.message_box.toPlainText()
		if feedbacker_msg == '' and feedbacker_name == '':
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Critical)
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap("Bin/Icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			msg.setWindowIcon(icon)
			msg.setStyleSheet("QLabel{font-size: 18px;} QPushButton{ width:60px; font-size: 18px; }")
			msg.setText("Error: Please fill up the form before sending")
			msg.setWindowTitle("Error")
			msg.exec_()
		else:
			firebaseConfig = {
			'apiKey': "AIzaSyBBCqEQTS8lDsiVauwdZyWQbrNcEGkKku4",
			'authDomain': "audiobookify-feedback.firebaseapp.com",
			'databaseURL': "https://audiobookify-feedback-default-rtdb.firebaseio.com",
			'projectId': "audiobookify-feedback",
			'storageBucket': "audiobookify-feedback.appspot.com",
			'messagingSenderId': "310337948554",
			'appId': "1:310337948554:web:bc557dcf0f45d21dc15673"
			}
			firebase = pyrebase.initialize_app(firebaseConfig)
			database = firebase.database()
			message = {"Message":feedbacker_msg}
			database.child("Feedbacks").child(feedbacker_name).set(message)
			self.ui.name_box.setText('')
			self.ui.message_box.setText('')

	def defaults_saves(self):
		path = 'Bin/Files/settings.config'
		abspath = os.path.abspath(path)
		quality = self.ui.quality_box.currentText()
		voice = self.ui.voice_box.currentText()
		file_type = self.ui.file_type_box.currentText()
		f = open(abspath, 'w')
		f.write(voice + '\n' + file_type + '\n' + quality + '\n' + imported_gui_mode)
		f.close()
		os.execl(sys.executable, sys.executable, *sys.argv)
	
	def light_mode_stw(self):
		path = 'Bin/Files/settings.config'
		abspath = os.path.abspath(path)
		f = open(abspath, 'r')
		line_3 = f.readlines()
		line_3[3] = 'Light Mode'
		f.close()
		f = open(abspath, 'w')
		f.writelines(line_3)
		f.close()
		os.execl(sys.executable, sys.executable, *sys.argv)
	
	def dark_mode_stw(self):
		path = 'Bin/Files/settings.config'
		abspath = os.path.abspath(path)
		f = open(abspath, 'r')
		line_3 = f.readlines()
		line_3[3] = 'Dark Mode'
		f.close()
		f = open(abspath, 'w')
		f.writelines(line_3)
		f.close()
		os.execl(sys.executable, sys.executable, *sys.argv)

	def retranslateUi(self, main_window):
		_translate = QtCore.QCoreApplication.translate
		main_window.setWindowTitle(_translate("main_window", "AudioBookify"))
		self.title_text.setText(_translate("main_window", "AudioBookify"))
		self.text_option_1.setPlaceholderText(_translate("main_window", "Type your text here or select a PDF/TXT file from below......"))
		self.text_option_2.setPlaceholderText(_translate("main_window", "Directory of the selected file"))
		self.select_file_btn.setText(_translate("main_window", "Select File"))
		self.advanced_label.setText(_translate("main_window", "Advanced Options"))
		self.info_btn.setText(_translate("main_window", "?"))
		self.voice_label.setText(_translate("main_window", "Voice"))
		self.gender_selector.setItemText(0, _translate("main_window", "Male Voice"))
		self.gender_selector.setItemText(1, _translate("main_window", "Female Voice"))
		self.file_label.setText(_translate("main_window", "File"))
		self.file_selector.setItemText(0, _translate("main_window", "MP3"))
		self.file_selector.setItemText(1, _translate("main_window", "WAV"))
		self.file_selector.setItemText(2, _translate("main_window", "OGG"))
		self.quality_selector.setItemText(0, _translate("main_window", "Excellent Quality"))
		self.quality_selector.setItemText(1, _translate("main_window", "Medium Quality"))
		self.quality_selector.setItemText(2, _translate("main_window", "Normal Quality"))

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	main_window = QtWidgets.QMainWindow()
	ui = Ui_main_window()
	ui.setupUi(main_window)
	main_window.show()
	sys.exit(app.exec_())