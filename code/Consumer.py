####################################################
#  D1014636 潘子珉
####################################################
import time
import socket
import eel
eel.init('gui', allowed_extensions=['.js', '.html'])

BUF_SIZE = 1024


port = 8881

@eel.expose
def get(serverIP):
    cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cSocket.connect((serverIP, port))
    cSocket.setblocking(False)
    time.sleep(0.2)
    while 1:
        try:
            server_reply = cSocket.recv(BUF_SIZE)
            data = server_reply.decode('utf-8')
            print(data)
            eel.writeMsg(1, data)
            break
        except BlockingIOError:
            pass
        time.sleep(2)
        eel.writeMsg(5, '資料等待中')
        print("資料等待中")
    cSocket.close()

eel.start('Consumer.html', size=(500, 500),port=0)  # Start