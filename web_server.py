'''
This implements a simple webserver that runs on port 8888 on your local machine.
You can use Firefox to connect to it 
It accepts only one connection at a time
'''
from socket import *

def create_webserver():
	server_socket = socket(AF_INET,SOCK_STREAM)
	try:
		server_socket.bind(("localhost",8888))
		server_socket.listen(5)
		while(1):
			(client_socket,address) = server_socket.accept()

			rd = client_socket.recv(128).decode()
			pieces = rd.split("\n")
			if len(pieces) > 0:
				print(pieces)
			
			data = "HTTP/1.1 200 OK\r\n"
			data += "Content-Type: text/html; charset=utf-8\r\n"
			data += "\r\n"
			data += "<html><body><h1>PYTHON ROCK!</h1><br><p>This is a Webserver</p></body></html>\r\n\r\n"
			client_socket.sendall(data.encode())
			client_socket.shutdown(SHUT_WR)
	except:
		print("Shutdown\n")
	server_socket.close()

print("Access http://localhost:8888")
create_webserver()
