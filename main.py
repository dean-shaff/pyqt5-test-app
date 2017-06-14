import sys

from PyQt5 import QtGui, QtCore, QtWidgets

from app.test_app import Ui_TestGUI

class TestGUI(QtWidgets.QMainWindow):

    def __init__(self, parent=None):

        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_TestGUI()
        self.ui.setupUi(self)

        self.QMainWindow = QtWidgets.QMainWindow(self)
        self.main_widget = QtWidgets.QWidget(self)
        self.__connect()

    def __connect(self):

        self.ui.button.clicked.connect(self.dummy)
        self.ui.button.clicked.connect(self.toggle_led)
        self.ui.led.off()

    @QtCore.pyqtSlot()
    def dummy(self):
        print("Dummy SLOT activated")

    @QtCore.pyqtSlot()
    def toggle_led(self):
        print("Toggling LED.")
        self.ui.led.toggleState()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = TestGUI()
    gui.show()
    app.exec_()
