import socket
import sys
import threading

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QStackedWidget, QListWidget
from PyQt5 import QtWidgets
import app_ui, rules_ui, computer_ui, game, game_computer

class Rules(QMainWindow, rules_ui.Ui_Form):
    def __init__(self):
        super(Rules, self).__init__()
        self.setupUi(self)



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
        self.show()

    def nickname_was_chosen(self):
        self.play.setEnabled(True)
        self.radioComputer.setEnabled(True)
        self.nickName.setEnabled(False)
        self.radioPeople.setEnabled(True)

    def play_was_clicked(self):
        self.name = self.nickName.text()
        # self.w = None
        print(self.name)
        if self.radioPeople.isChecked():
            pass
        elif self.radioComputer.isChecked():
            self.hide()
            self.openWindow()
        else:
            pass

    def show_rules(self):
        self.dialog = Rules()
        self.dialog.show()







if __name__ == "__main__":
    # при запуске клиента мы создаем инстанс приложения, созданного нами главного окна, и все запускаем
    app = QApplication(sys.argv)
    window = Menu()
    sys.exit(app.exec_())

    # pyuic5 name.ui -o name.py
