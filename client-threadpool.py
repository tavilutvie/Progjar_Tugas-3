import concurrent.futures
import socket
import sys

def get_time(address, port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((address, port))
        request = 'TIME\r\n'
        client_socket.send(request.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(response)
        client_socket.close()
    except socket.error as e:
        print("Error: ", e)
        sys.exit()

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(10):
            executor.submit(get_time, '172.18.0.2', 45000)
