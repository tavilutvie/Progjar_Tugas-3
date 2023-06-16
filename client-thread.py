import threading
import socket
import sys

class ClientThread(threading.Thread):
    def __init__(self, address, port):
        threading.Thread.__init__(self)
        self.address = address
        self.port = port

    def run(self):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((self.address, self.port))
            request = 'TIME\r\n'
            client_socket.send(request.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            print(response)
            client_socket.close()
        except socket.error as e:
            print("Error: ", e)
            sys.exit()

if __name__ == '__main__':
    for i in range(10):
        thread = ClientThread('172.18.0.2', 45000)
        thread.start()
