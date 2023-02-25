import socket
import threading

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import app_ui, rules_ui, computer, people
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
        self.window = ComputerGame()
        self.window.show()

    def openWindowPeople(self):
        self.window = PeopleGame()
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



class ComputerGame(QMainWindow, computer.Ui_SecondWindow):
    def __init__(self):
        super(ComputerGame, self).__init__()
        self.setupUi(self)
        self.send_clicked = False
        self.returnButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnButton.setGeometry(QtCore.QRect(190, 210, 130, 32))
        self.returnButton.setText('Back to Menu')
        self.easy.clicked.connect(lambda x: self.textBrowser.setText('4 digits 10 attempts'))
        self.medium.clicked.connect(lambda x: self.textBrowser.setText('5 digits 8 attempts'))
        self.hard.clicked.connect(lambda x: self.textBrowser.setText('6 digits 8 attempts'))
        self.pushButton.clicked.connect(self.start_game)
        self.sendButton.clicked.connect(self.game)
        self.returnButton.clicked.connect(self.back_to_menu)


    def send_was_clicked(self):
        self.send_clicked = True

    def start_game(self):
        self.number.setText("Write number")
        self.pushButton.setEnabled(False)
        self.number.setEnabled(True)
        self.sendButton.setEnabled(True)
        if self.easy.isChecked():
            self.attempts = 10
            self.length = 4
        elif self.medium.isChecked():
            self.attempts = 8
            self.length = 5
        else:
            self.attempts = 8
            self.length = 6
        self.right_num = game.get_number(self.length)
        self.i = 0


    def game(self):
        self.send_clicked = False
        if game.is_available_numbers(self.number.text(), self.length):
            self.i += 1
            try_num = self.number.text()
            self.number.setText('')
            self.number.setEnabled(False)
            self.sendButton.setEnabled(False)
            bulls, cows = game.get_bulls_and_cows_from_number(self.right_num, try_num)
            if bulls == 4 and str(try_num) == str(self.right_num):
                self.tableWidget.setStyleSheet("QTableWidget {\n"
                                               "\n"
                                               "background-color:rgb(0, 255, 0)\n"
                                               "  \n"
                                               "\n"
                                               "\n"
                                               "\n"
                                               "}")
                self.number.setText("WIN {}".format(self.right_num))
                self.pushButton.setEnabled(True)
            else:
                self.tableWidget.setItem(self.i, 0, QTableWidgetItem(str(bulls)))
                self.tableWidget.setItem(self.i, 1, QTableWidgetItem(str(cows)))
                self.tableWidget.setItem(self.i, 2, QTableWidgetItem(str(try_num)))
                self.attempts -= 1
                print(bulls, cows)
                print(self.right_num)
                print(self.attempts)
                self.number.setEnabled(True)
                self.sendButton.setEnabled(True)
            if self.attempts == 0:
                self.number.setText("Right_num {}".format(self.right_num))
                self.tableWidget.setStyleSheet("QTableWidget {\n"
                                               "\n"
                                               "background-color:rgb(255, 0, 0)\n"
                                               "  \n"
                                               "\n"
                                               "\n"
                                               "\n"
                                               "}")

                self.number.setEnabled(False)
                self.sendButton.setEnabled(False)
                self.pushButton.setEnabled(True)
        else:
            self.number.setText("Not right number")

    def back_to_menu(self):
        Menu.window = Menu()
        self.close()

class PeopleGame(QMainWindow, people.Ui_ThirdWindow):
    def __init__(self):
        super(PeopleGame, self).__init__()
        self.setupUi(self)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 5010))
        self.returnButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnButton.setGeometry(QtCore.QRect(250, 150, 130, 32))
        self.returnButton.setText('Back to Menu')
        self.returnButton.setEnabled(False)
        self.sendButton.clicked.connect(self.write)
        self.send_button.clicked.connect(self.send)
        self.returnButton.clicked.connect(self.back_to_menu)
        self.show()
        self.stop_thread = False

    def send(self):
        guess_number = self.guess_number.text()
        if game.is_available_numbers(guess_number, 4):
            self.client.send(f's{guess_number}'.encode('ascii'))
            self.guess_number.setEnabled(False)
            self.send_button.setEnabled(False)
            self.number.setEnabled(True)
            self.sendButton.setEnabled(True)
            receive_thread = threading.Thread(target=self.receive)
            receive_thread.start()
        else:
            self.guess_number.setText('Incorrect number')


    def write(self):
        message = self.number.text()
        self.client.send(message.encode('ascii'))
        self.number.setText('Wait your opponent')
        self.sendButton.setEnabled(False)

    def receive(self):
        while not self.stop_thread:
            try:
                message = self.client.recv(1024).decode('ascii')
                if message == 'f':
                    self.messages.append('LOSE')
                    self.sendButton.setEnabled(False)
                    self.returnButton.setEnabled(True)
                elif message == 'w':
                    self.messages.append('WIN')
                    self.sendButton.setEnabled(False)
                    self.returnButton.setEnabled(True)
                elif message == 'ready':
                    self.number.setText('Go')
                    self.sendButton.setEnabled(True)
                elif message == 'i':
                    self.number.setText('Incorrect input')
                    self.sendButton.setEnabled(True)
                else:
                    message = message.split()
                    print(message)
                    self.messages.append(f'{message[0]} | {message[1]} | {message[2]}')
            except:
                print('error')

    def back_to_menu(self):
        self.stop_thread = True
        self.close()
        Menu.window = Menu()
        self.client.close()


if __name__ == "__main__":
    app = QApplication([])
    window = Menu()
    app.exec()
