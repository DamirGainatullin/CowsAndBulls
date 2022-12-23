import sys
import threading

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QStackedWidget, QListWidget
from PyQt5 import QtWidgets
import app_ui, rules_ui, computer, people
import people2


class Rules(QMainWindow, rules_ui.Ui_Form):
    def __init__(self):
        super(Rules, self).__init__()
        self.setupUi(self)
class Menu(QMainWindow, app_ui.Ui_MainWindow):
    def __init__(self):
        # в методе инициализации мы вызываем родительскую инициализацию (устанавливаем элементы интерфейса)
        super(Menu, self).__init__()
        self.setupUi(self)
        self.ok.clicked.connect(self.nickname_was_chosen)
        self.pushButton.clicked.connect(self.show_rules)
        self.play.clicked.connect(self.play_was_clicked)
        self.show()

    def openWindowCom(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = computer.Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindowPeople2(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui2 = people.Ui_ThirdWindow()
        # people.get_name(self.nickName.text())
        self.ui2.setupUi(self.window2)
        self.window2.show()


    def openWindowPeople1(self):
        self.window1 = QtWidgets.QMainWindow()
        self.ui1 = people2.Ui_FiveWindow()
        # people.get_name(self.nickName.text())
        self.ui1.setupUi(self.window1)
        self.window1.show()

    def nickname_was_chosen(self):
        self.play.setEnabled(True)
        self.radioComputer.setEnabled(True)
        self.nickName.setEnabled(False)
        self.radioPeople.setEnabled(True)

    def play_was_clicked(self):
        self.name = self.nickName.text()
        if self.radioPeople.isChecked():
            self.hide()
            self.openWindowPeople1()
            self.openWindowPeople2()
        elif self.radioComputer.isChecked():
            self.hide()
            self.openWindowCom()

        else:
            pass

    def show_rules(self):
        self.dialog = Rules()
        self.dialog.show()

    # def lvl_was_clicked(self):
    #     pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Menu()
    sys.exit(app.exec_())
