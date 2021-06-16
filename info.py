from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_info_window(object):
	def setupUi(self, info_window):
		info_window.setObjectName("info_window")
		info_window.resize(411, 415)
		info_window.setMaximumSize(QtCore.QSize(411, 415))
		info_window.setMinimumSize(QtCore.QSize(411, 415))
		font = QtGui.QFont()
		font.setFamily("Verdana")
		info_window.setFont(font)
		info_window.setStyleSheet("background-color: rgb(79, 80, 81);\n"
"border-radius: 9px;")
		flags = QtCore.Qt.WindowFlags(QtCore.Qt.WindowStaysOnTopHint)
		info_window.setWindowFlags(flags)
		info_window.setWindowFlags(info_window.windowFlags() & QtCore.Qt.CustomizeWindowHint)
		info_window.setWindowFlags(info_window.windowFlags() & ~QtCore.Qt.WindowMinMaxButtonsHint)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("Bin/Icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		info_window.setWindowIcon(icon)
		self.centralwidget = QtWidgets.QWidget(info_window)
		self.centralwidget.setObjectName("centralwidget")
		self.logo = QtWidgets.QLabel(self.centralwidget)
		self.logo.setGeometry(QtCore.QRect(100, 10, 201, 191))
		self.logo.setText("")
		self.logo.setPixmap(QtGui.QPixmap("Bin/Icons/logo.png"))
		self.logo.setScaledContents(True)
		self.logo.setAlignment(QtCore.Qt.AlignCenter)
		self.logo.setObjectName("logo")
		self.frame = QtWidgets.QFrame(self.centralwidget)
		self.frame.setGeometry(QtCore.QRect(-10, 279, 450, 421))
		self.frame.setStyleSheet("background-color: rgb(255, 84, 84);")
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.guide_button = QtWidgets.QPushButton(self.frame)
		self.guide_button.setGeometry(QtCore.QRect(100, 10, 231, 23))
		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		font.setPointSize(10)
		self.guide_button.setFont(font)
		self.guide_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(82, 183, 255);\n"
"border: 0px solid rgb(255, 84, 84);\n"
"border-radius: 5px;")
		self.guide_button.setObjectName("guide_button")
		self.guide_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.label_3 = QtWidgets.QLabel(self.frame)
		self.label_3.setGeometry(QtCore.QRect(20, 40, 151, 81))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_3.setFont(font)
		self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.label_3.setObjectName("label_3")
		self.label = QtWidgets.QLabel(self.frame)
		self.label.setGeometry(QtCore.QRect(310, 40, 101, 81))
		self.label.setText("Audiobookify")
		self.label.setPixmap(QtGui.QPixmap("Bin/Icons/rotary76.png"))
		self.label.setScaledContents(True)
		self.label.setObjectName("label")
		self.title = QtWidgets.QLabel(self.centralwidget)
		self.title.setGeometry(QtCore.QRect(30, 190, 351, 71))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(24)
		font.setBold(True)
		font.setWeight(75)
		self.title.setFont(font)
		self.title.setStyleSheet("color: rgb(82, 183, 255);")
		self.title.setAlignment(QtCore.Qt.AlignCenter)
		self.title.setObjectName("title")
		info_window.setCentralWidget(self.centralwidget)

		self.retranslateUi(info_window)
		QtCore.QMetaObject.connectSlotsByName(info_window)

	def retranslateUi(self, info_window):
		_translate = QtCore.QCoreApplication.translate
		info_window.setWindowTitle(_translate("info_window", "Information"))
		self.guide_button.setText(_translate("info_window", "Read the full guide"))
		self.label_3.setText(_translate("info_window", "Coder: Arib Muhtasim\n"
"Styling and design:\n"
"  Junaid Bin Saiful\n"
"  Zawata Afnan Zenith\n"
"  Arefin Islam Rafat"))
		self.title.setText(_translate("info_window", "AudioBookify"))


if __name__ == "__main__":
	import sys
	info_window_app = QtWidgets.QApplication(sys.argv)
	info_window = QtWidgets.QMainWindow()
	ui = Ui_info_window()
	ui.setupUi(info_window)
	info_window.show()
	sys.exit(info_window_app.exec_())