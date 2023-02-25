import threading
import game

host, port = "0.0.0.0", 5010

import socket

sock = socket.socket()
sock.bind((host, port))
sock.listen(2)
first_player_number = 0
second_player_number = 0
players = []

def check_and_send(number, conn):
    if game.is_available_numbers(number, 4):
        if conn == players[0]:
            bulls, cows = game.get_bulls_and_cows_from_number(second_player_number ,number)
            print(bulls, cows)
            if bulls == 4:
                players[1].send('f'.encode('ascii'))
                players[0].send('w'.encode('ascii'))
            else:
                players[0].send(f'{bulls} {cows} {number}'.encode('ascii'))
                players[1].send('ready'.encode('ascii'))
        else:
            bulls, cows = game.get_bulls_and_cows_from_number(first_player_number ,number)
            if bulls == 4:
                players[0].send('f'.encode('ascii'))
                players[1].send('w'.encode('ascii'))
            else:
                players[1].send(f'{bulls} {cows} {number}'.encode('ascii'))
                players[0].send('ready'.encode('ascii'))
    else:
        conn.send('i'.encode('ascii'))


def handle(conn):
    print('handle', conn)
    while True:
        try:
            number = conn.recv(1024).decode('ascii')
            check_and_send(number, conn)
        except:
            conn.close()


while True:
    conn, addr = sock.accept()
    print(conn, addr)
    players.append(conn)
    data = conn.recv(1024).decode('ascii')
    if data[0] == 's':
        if first_player_number == 0:
            first_player_number = data[1:]
        else:
            second_player_number = data[1:]
        print(first_player_number, second_player_number)
        thread = threading.Thread(target=handle, args=(conn,))
        thread.start()



