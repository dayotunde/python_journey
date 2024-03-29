'''
This application mimics the behaviour of a simple web browser in python.
It executes a GET request to data.pr4e.org and returns page1.htm
'''
import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("data.pr4e.org",80))
cmd = "GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n" .encode()
my_socket.send(cmd)

while True:
    data = my_socket.recv(128)
    if len(data)<1:
        break
    print(data.decode(),end="")

my_socket.close()
