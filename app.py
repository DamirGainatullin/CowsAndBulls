import socket
import threading

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

import app_ui, rules_ui, computer_ui

class Rules(QWidget, rules_ui.Ui_Form):
    def __init__(self):
        super().__init__()
        # в методе инициализации мы вызываем родительскую инициализацию (устанавливаем элементы интерфейса)
        self.setupUi(self)

class Computer(QWidget, computer_ui.Ui_Form):
    def __int__(self):
        super().__int__()
        self.setupUi(self)

class Menu(QMainWindow, app_ui.Ui_MainWindow):
    def __init__(self):
        # в методе инициализации мы вызываем родительскую инициализацию (устанавливаем элементы интерфейса)
        super(Menu, self).__init__()
        self.setupUi(self)
        self.ok.clicked.connect(self.nickname_was_chosen)
        self.pushButton.clicked.connect(self.show_rules)
        self.play.clicked.connect(self.play_was_clicked)

    def nickname_was_chosen(self):
        self.play.setEnabled(True)
        self.radioComputer.setEnabled(True)
        self.nickName.setEnabled(False)
        self.radioPeople.setEnabled(True)

    def play_was_clicked(self):
        self.name = self.nickName.text()
        if self.radioPeople.isChecked():
            pass
        elif self.radioComputer.isChecked():
            self.comp_dialog = Computer()
            self.comp_dialog.show()
        else:
            pass

    def show_rules(self):
        self.dialog = Rules()
        self.dialog.show()





if __name__ == "__main__":
    # при запуске клиента мы создаем инстанс приложения, созданного нами главного окна, и все запускаем
    app = QApplication([])
    window = Menu()
    window.show()
    app.exec()

    # pyuic5 name.ui -o name.py
