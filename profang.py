#!python3

# System modules
import sys

# UI
import qt_uis.ui_mainwindow

# Qt libs
from PySide2 import QtCore, QtWidgets, QtGui, QtUiTools

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = qt_uis.ui_mainwindow.Ui_MainWindow()
		self.ui.setupUi(self)

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	widget = MainWindow()
	widget.resize(1600, 900)
	widget.show()

	sys.exit(app.exec_())
	