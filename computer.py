# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(567, 637)
        SecondWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(95, 95, 95);\n"
"    color: rgb(250, 250, 250);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 180, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 280, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.easy = QtWidgets.QRadioButton(self.centralwidget)
        self.easy.setGeometry(QtCore.QRect(20, 90, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.easy.setFont(font)
        self.easy.setObjectName("easy")
        self.hard = QtWidgets.QRadioButton(self.centralwidget)
        self.hard.setGeometry(QtCore.QRect(20, 150, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.hard.setFont(font)
        self.hard.setObjectName("hard")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setObjectName("label")
        self.number = QtWidgets.QLineEdit(self.centralwidget)
        self.number.setEnabled(False)
        self.number.setGeometry(QtCore.QRect(170, 280, 121, 31))
        self.number.setObjectName("number")
        self.medium = QtWidgets.QRadioButton(self.centralwidget)
        self.medium.setGeometry(QtCore.QRect(20, 120, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.medium.setFont(font)
        self.medium.setObjectName("medium")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 320, 371, 291))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QWidget {\n"
"    border: none;\n"
"    color: rgb(250, 250, 250);\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(190, 90, 361, 111))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setEnabled(False)
        self.sendButton.setGeometry(QtCore.QRect(300, 280, 93, 28))
        self.sendButton.setIconSize(QtCore.QSize(16, 16))
        self.sendButton.setAutoRepeatInterval(100)
        self.sendButton.setObjectName("sendButton")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        # actions
        # self.easy.clicked.connect(lambda x: self.textBrowser.setText('4 digits 10 attempts'))
        # self.medium.clicked.connect(lambda x: self.textBrowser.setText('5 digits 8 attempts'))
        # self.hard.clicked.connect(lambda x: self.textBrowser.setText('6 digits 8 attempts'))
        # self.pushButton.clicked.connect(lambda x: self.start_game())

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)
    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.pushButton.setText(_translate("SecondWindow", "Start"))
        self.label_3.setText(_translate("SecondWindow", "Write your number"))
        self.easy.setText(_translate("SecondWindow", "Easy"))
        self.hard.setText(_translate("SecondWindow", "Hard"))
        self.label.setText(_translate("SecondWindow", "PLay With Computer"))
        self.number.setText(_translate("SecondWindow", "1234"))
        self.medium.setText(_translate("SecondWindow", "Medium"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("SecondWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SecondWindow", "Bulls"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SecondWindow", "Cows"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SecondWindow", "Number"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("SecondWindow", "start"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("SecondWindow", "start"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("SecondWindow", "start"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("SecondWindow", "Set game parametres:"))
        self.textBrowser.setHtml(_translate("SecondWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Console\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\">DESCRIPTION:</span></p></body></html>"))
        self.sendButton.setText(_translate("SecondWindow", "Send"))

    def start_game(self):
        self.sendButton.setEnabled(True)
        self.flag = False
        #game
        #generate number
        while self.flag:
            self.number.text()
        #QTableWidget