import socket
import threading

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

import app_ui, rules_ui, computer_ui, game

class Rules(QWidget, rules_ui.Ui_Form):
    def __init__(self):
        super().__init__()
        # в методе инициализации мы вызываем родительскую инициализацию (устанавливаем элементы интерфейса)
        self.setupUi(self)

class Computer(QWidget, computer_ui.Ui_Form):
    def __int__(self):
        super().__int__()
        self.setupUi(self)
        self.pushButton.setEnabled(False)
        if self.easy.isChecked():
            self.pushButton.setEnabled(True)
            self.easy_game()
        elif self.medium.isChecked():
            self.pushButton.setEnabled(True)
            self.medium_game()
        else:
            self.pushButton.setEnabled(True)
            self.hard_game()

    def easy_game(self):
        self.number.setEnabled(True)
        self.textBrowser.setText('4 symbols, 7 attempts ,only digits')
        self.answer = game.get_number(4)
        pass

    def medium_game(self):
        self.number.setEnabled(True)
        self.textBrowser.setText('4 symbols, 5 attempts only digits')
        self.answer = game.get_number(4)
        pass


    def hard_game(self):
        self.number.setEnabled(True)
        self.answer = game.get_number(5)
        self.textBrowser.setText('5 symbols, 5 attempts digits and letter') # а может все таки ну эти буквы...




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
            self.comp_dialog.setupUi(self.comp_dialog)
            self.comp_dialog.show()
        else:
            pass

    def show_rules(self):
        self.dialog = Rules()
        self.dialog.setupUi(self.dialog)
        self.dialog.show()





if __name__ == "__main__":
    # при запуске клиента мы создаем инстанс приложения, созданного нами главного окна, и все запускаем
    app = QApplication([])
    window = Menu()
    window.show()
    app.exec()

    # pyuic5 name.ui -o name.py
