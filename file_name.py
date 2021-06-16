from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_File_picker(object):
	def setupUi(self, file_name_window):
		file_name_window.setObjectName("file_name_window")
		file_name_window.resize(420, 91)
		file_name_window.setStyleSheet("background-color: rgb(255, 255, 255);\n"
	"border:2px solid;")
		file_name_window.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.centralwidget = QtWidgets.QWidget(file_name_window)
		self.centralwidget.setObjectName("centralwidget")
		self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
		self.cancel_btn.setGeometry(QtCore.QRect(340, 60, 75, 23))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(9)
		self.cancel_btn.setFont(font)
		self.cancel_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.cancel_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
	"border: 2px solid black;\n"
	"border-radius: 5px;")
		self.cancel_btn.setObjectName("cancel_btn")
		self.final_export_btn = QtWidgets.QPushButton(self.centralwidget)
		self.final_export_btn.setGeometry(QtCore.QRect(260, 60, 75, 23))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(9)
		self.final_export_btn.setFont(font)
		self.final_export_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.final_export_btn.setStyleSheet("background-color: rgb(13, 118, 222);\n"
	"color: rgb(255, 255, 255);\n"
	"border: 0 px solid;\n"
	"border-radius: 5px;")
		self.final_export_btn.setObjectName("final_export_btn")
		self.file_name_picked = QtWidgets.QLineEdit(self.centralwidget)
		self.file_name_picked.setGeometry(QtCore.QRect(10, 10, 401, 31))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(12)
		self.file_name_picked.setFont(font)
		self.file_name_picked.setStyleSheet("background-color: rgb(13, 118, 222);\n"
	"color: rgb(255, 255, 255);\n"
	"border: 0 px solid;\n"
	"border-radius: 5px;")
		self.file_name_picked.setMaxLength(20)
		self.file_name_picked.setCursorPosition(0)
		self.file_name_picked.setClearButtonEnabled(True)
		self.file_name_picked.setObjectName("file_name_picked")
		file_name_window.setCentralWidget(self.centralwidget)

		self.retranslateUi(file_name_window)
		QtCore.QMetaObject.connectSlotsByName(file_name_window)

	def retranslateUi(self, file_name_window):
		_translate = QtCore.QCoreApplication.translate
		file_name_window.setWindowTitle(_translate("file_name_window", "file_name_window"))
		self.cancel_btn.setText(_translate("file_name_window", "Cancel"))
		self.final_export_btn.setText(_translate("file_name_window", "Export"))
		self.file_name_picked.setPlaceholderText(_translate("file_name_window", " Enter the name of your file"))

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	file_name_window = QtWidgets.QMainWindow()
	ui = Ui_File_picker()
	ui.setupUi(file_name_window)
	file_name_window.show()
	sys.exit(app.exec_())
