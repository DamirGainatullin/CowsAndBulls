# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'computerui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(607, 684)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("QWidget {\n"
"    background-color:rgb(95, 95, 95);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color:black;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 10, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.easy = QtWidgets.QRadioButton(Form)
        self.easy.setGeometry(QtCore.QRect(30, 90, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.easy.setFont(font)
        self.easy.setObjectName("easy")
        self.medium = QtWidgets.QRadioButton(Form)
        self.medium.setGeometry(QtCore.QRect(30, 120, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.medium.setFont(font)
        self.medium.setObjectName("medium")
        self.hard = QtWidgets.QRadioButton(Form)
        self.hard.setGeometry(QtCore.QRect(30, 150, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.hard.setFont(font)
        self.hard.setObjectName("hard")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 180, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(200, 90, 361, 111))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 280, 151, 31))
        self.label_3.setObjectName("label_3")
        self.number = QtWidgets.QLineEdit(Form)
        self.number.setEnabled(False)
        self.number.setGeometry(QtCore.QRect(180, 280, 121, 31))
        self.number.setObjectName("number")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(40, 330, 281, 291))
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
"    color: rgb(10, 10, 10);\n"
"    font-size: 14px;\n"
"    font-color: white;\n"
"}\n"
"")
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "PLay With Computer"))
        self.label_2.setText(_translate("Form", "Set game parametres:"))
        self.easy.setText(_translate("Form", "Easy"))
        self.medium.setText(_translate("Form", "Medium"))
        self.hard.setText(_translate("Form", "Hard"))
        self.pushButton.setText(_translate("Form", "Start"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Console\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\">DESCRIPTION:</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "Write your numer"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Bulls"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Cows"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "start"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "start"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
