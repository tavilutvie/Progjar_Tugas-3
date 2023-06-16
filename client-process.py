import multiprocessing as mp
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
    processes = []
    for i in range(10):
        process = mp.Process(target=get_time, args=('172.18.0.2', 45000))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
