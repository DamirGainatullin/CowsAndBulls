import socket
import sys
import threading

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import app_ui, rules_ui, computer, people
import people
import game


class Rules(QMainWindow, rules_ui.Ui_Form):
    def __init__(self):
        super(Rules, self).__init__()
        self.setupUi(self)

class Menu(QMainWindow, app_ui.Ui_MainWindow):
    def __init__(self):
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

    def openWindowPeople(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = people.Ui_ThirdWindow()
        # people.get_name(self.nickName.text())
        self.ui.setupUi(self.window)
        self.window.show()



    def nickname_was_chosen(self):
        self.play.setEnabled(True)
        self.radioComputer.setEnabled(True)
        self.nickName.setEnabled(False)
        self.radioPeople.setEnabled(True)

    def play_was_clicked(self):
        self.name = self.nickName.text()
        if self.radioPeople.isChecked():
            self.hide()
            self.openWindowPeople()
        elif self.radioComputer.isChecked():
            self.hide()
            self.openWindowCom()

        else:
            pass

    def show_rules(self):
        self.dialog = Rules()
        self.dialog.show()

#
# class PeopleGame(QMainWindow, people.Ui_ThirdWindow):
#     def __init__(self):
#         super(PeopleGame, self).__init__()
#         self.setupUi(self)
#         self.sendButton.clicked.connect(self.write)
#         self.send_button.clicked.connect(self.send)
#         self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.client.connect(('127.0.0.1', 5010))
#         self.show()
#     #
    # def send(self):
    #     guess_number = self.guess_number.text()
    #     if game.is_available_numbers(guess_number, 4):
    #         self.client.send(f's{guess_number}'.encode('ascii'))
    #         self.guess_number.setEnabled(False)
    #         self.send_button.setEnabled(False)
    #         self.number.setEnabled(True)
    #         self.sendButton.setEnabled(True)
    #         receive_thread = threading.Thread(target=self.receive)
    #         receive_thread.start()
    #     else:
    #         self.guess_number.setText('Incorrect number')
    #
    #
    # def write(self):
    #     message = self.number.text()
    #     self.client.send(message.encode('ascii'))
    #     self.sendButton.setEnabled(False)
    #
    # def receive(self):
    #     print(1)
    #     while True:
    #         try:
    #             # пытаемся получить сообщение
    #             message = self.client.recv(1024).decode('ascii')
    #             print(message, message == 'wait')
    #             if message == 'f':
    #                 self.messages.append('LOSE')
    #             elif message == 'w':
    #                 self.messages.append('WIN')
    #             else:
    #                 self.sendButton.setEnabled(True)
    #                 message = message.split()
    #                 print(message)
    #                 self.messages.append(f'{message[0]} | {message[1]} | {message[2]}')
    #                 # self.sendButton.setEnabled(False)
    #         except:
    #             print('error')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # server
    window = Menu()

    sys.exit(app.exec_())
