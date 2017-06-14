# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './app/test_app.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TestGUI(object):
    def setupUi(self, TestGUI):
        TestGUI.setObjectName("TestGUI")
        TestGUI.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TestGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.button = QtWidgets.QPushButton(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
        self.button.setSizePolicy(sizePolicy)
        self.button.setObjectName("button")
        self.gridLayout.addWidget(self.button, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 2, 0, 1, 3)
        self.led = LedWidget(self.gridWidget)
        self.led.setProperty("diameter", 18)
        self.led.setProperty("color", QtGui.QColor(0, 255, 0))
        self.led.setProperty("state", True)
        self.led.setObjectName("led")
        self.gridLayout.addWidget(self.led, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout_2.addWidget(self.gridWidget, 0, 0, 1, 1)
        TestGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TestGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        TestGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TestGUI)
        self.statusbar.setObjectName("statusbar")
        TestGUI.setStatusBar(self.statusbar)

        self.retranslateUi(TestGUI)
        QtCore.QMetaObject.connectSlotsByName(TestGUI)

    def retranslateUi(self, TestGUI):
        _translate = QtCore.QCoreApplication.translate
        TestGUI.setWindowTitle(_translate("TestGUI", "Test GUI"))
        self.button.setText(_translate("TestGUI", "Eu gosto de tudo"))

from .ledwidget import LedWidget
