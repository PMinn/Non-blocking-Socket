####################################################
#  D1014636 潘子珉
####################################################
import socket
import select
import queue

BUF_SIZE = 1024

q = queue.Queue(maxsize=5)

inputs = []
outputs = []
srv_list = []

# Create Producer Socket
Producer_PORT = 8880
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', Producer_PORT))
server.setblocking(False)
server.listen(5)
inputs.append(server)
srv_list.append(server)
print("Producer listening on port " + str(Producer_PORT))

# Create Producer Socket
Consumer_PORT = 8881
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', Consumer_PORT))
server.setblocking(False)
server.listen(5)
inputs.append(server)
srv_list.append(server)
print("Consumer listening on port " + str(Consumer_PORT))

print("Waiting incomming connection ...")
	
while True:
	readable, writable, exceptional = select.select(inputs, outputs, inputs)
	for s in readable:
		if s in srv_list: # is server socket
			connection, (rip, rport) = s.accept()
			connection.setblocking(False)
			laddr = connection.getsockname()
			if laddr[1] == Producer_PORT:
				inputs.append(connection)
				msg = "Accept Producer connection from (%s, %d)" %(str(rip), rport)
				print(msg)
			else:
				outputs.append(connection)
				msg = "Accept Consumer connection from (%s, %d)" %(str(rip), rport)
				print(msg)
		else: # is connecting client socket && Producer
			try:
				data = s.recv(BUF_SIZE)
				if data:
					raddr = s.getpeername()
					laddr = s.getsockname()
					if not q.full():
						q.put(int(data.decode('utf-8')))
						s.send("A".encode('utf-8'))
					else:
						s.send("E:Queue is Full".encode('utf-8'))
					print("Close connection from: ", raddr)
					inputs.remove(s)
					s.close()
			except ConnectionResetError:
				print("Connection reset by peer")
				pass
	for s in writable:
		try:
			if not q.empty():
				s.send(str(q.get()).encode('utf-8'))
				outputs.remove(s)
				s.close()
		except ConnectionResetError:
				print("Connection reset by peer")
				pass

	for s in exceptional:
		print("Close : ", s)
		inputs.remove(s)
		s.close()