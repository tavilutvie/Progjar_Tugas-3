import threading
import socket
import sys
import time
import logging

def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")
    
    server_address = ('localhost', 45000)
    logging.warning(f"opening socket {server_address}")
    
    sock.connect(server_address)

    try:
        # Send data
        message = 'TIME\r\n'
        logging.warning(f"[CLIENT] sending {message}")
        sock.sendall(message.encode('utf-8'))
        # Look for the response
        data = sock.recv(1024).decode('utf-8')
        logging.warning(f"[DITERIMA DARI SERVER] {data}")
    finally:
        logging.warning("closing")
        sock.close()
    return
if __name__=='__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(target=kirim_data)
        threads.append(t)
        t.start()
    print("Total thread yang terpakai: ", threading.active_count())
    for t in threads:
       t.join()
