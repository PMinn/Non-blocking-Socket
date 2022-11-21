####################################################
#  D1014636 潘子珉
####################################################
import socket
import eel
eel.init('gui', allowed_extensions=['.js', '.html'])

BUF_SIZE = 1024

port = 8880

@eel.expose
def send(serverIP, number):
    cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cSocket.connect((serverIP, port))

    cSocket.send(str(number).encode('utf-8'))

    server_reply = cSocket.recv(BUF_SIZE)
    server_reply = server_reply.decode('utf-8').split(':')
    if server_reply[0] == 'A':
        eel.writeMsg(0, f"send:{number} OK")
    else:
        eel.writeMsg(4, server_reply[1])
    cSocket.close()

eel.start('Producer.html', size=(500, 500),port=0)  # Start