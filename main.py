import socket
import json
import os
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cls = lambda: os.system('cls')
client.connect(('127.0.0.1', 2000))
client.send('FindGame'.encode('utf-8'))
print('Find apponent')
def polle(pole):
    cls()
    for i, item in enumerate(pole):
        match item:
            case 0: print('* ', end='')
            case 1: print('x ', end='')
            case 2: print('o ', end='')
        if (i + 1) % 3 == 0 and i != 1: print('\n')
def res(a):
    match a:
        case '1': return "6"
        case '2': return "7"
        case '3': return "8"
        case '4': return "3"
        case '5': return "4"
        case '6': return "5"
        case '7': return "0"
        case '8': return "1"
        case '9': return "2"
while True:
    move = client.recv(1024).decode('utf-8')
    if move == 'exit':
        break
    elif move == 'win':
        print('You win')
        break
    elif move == 'loose':
        print('You loose')
        break
    pole = json.loads(client.recv(1024).decode('utf-8'))
    polle(pole)
    if move == '1':
        a = input("> ")
        client.send(res(a).encode('utf-8'))
input()