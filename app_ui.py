from PyQt5 import QtCore, QtGui, QtWidgets

from computer import Ui_SecondWindow


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFocusPolicy(QtCore.Qt.WheelFocus)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color:rgb(95, 95, 95);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QWidget {\n"
"    background-color:rgb(95, 95, 95);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"    border-radius:15px;\n"
"    background-color:rgb(29, 31, 30);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(200, 200, 200);\n"
"}\n"
"")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 10, 321, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.nickName = QtWidgets.QLineEdit(self.centralwidget)
        self.nickName.setEnabled(True)
        self.nickName.setGeometry(QtCore.QRect(50, 90, 411, 31))
        self.nickName.setObjectName("nickName")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 10, 51, 51))
        self.pushButton.setMinimumSize(QtCore.QSize(0, 1))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 130, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.radioComputer = QtWidgets.QRadioButton(self.centralwidget)
        self.radioComputer.setEnabled(False)
        self.radioComputer.setGeometry(QtCore.QRect(130, 180, 151, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioComputer.sizePolicy().hasHeightForWidth())
        self.radioComputer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioComputer.setFont(font)
        self.radioComputer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioComputer.setObjectName("radioComputer")
        self.radioPeople = QtWidgets.QRadioButton(self.centralwidget)
        self.radioPeople.setEnabled(False)
        self.radioPeople.setGeometry(QtCore.QRect(310, 180, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioPeople.sizePolicy().hasHeightForWidth())
        self.radioPeople.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioPeople.setFont(font)
        self.radioPeople.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioPeople.setObjectName("radioPeople")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setEnabled(False)
        self.play.setGeometry(QtCore.QRect(230, 250, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.play.setFont(font)
        self.play.setObjectName("play")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(470, 90, 31, 28))
        self.ok.setObjectName("ok")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Bulls and Cows"))
        self.nickName.setText(_translate("MainWindow", "Write your name"))
        self.pushButton.setText(_translate("MainWindow", "?"))
        self.label_2.setText(_translate("MainWindow", "PLay with:"))
        self.radioComputer.setText(_translate("MainWindow", "Computer"))
        self.radioPeople.setText(_translate("MainWindow", "Other people"))
        self.play.setText(_translate("MainWindow", "PLay"))
        self.ok.setText(_translate("MainWindow", "OK"))
