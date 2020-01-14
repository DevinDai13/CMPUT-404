import socket, time
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)      
        s.bind((HOST, PORT))
        s.listen(2)
       
        while True:
            conn, addr = s.accept() #accept incoming connections
            p = Process(target=handle_echo, args=(conn, addr))
            p.daemon = True
            p.start()
            print("Started Process ", p)

def handle_echo(conn,addr):
    with conn:
       print("Connected by ", conn)
       full_data = b""
       while True:
           data = conn.recv(BUFFER_SIZE)
           if not data:
               break
           full_data += data
       time.sleep(0.5)
       conn.sendall(full_data)
       conn.shutdown(socket.SHUT_RDWR)
       conn.close()

if __name__ == "__main__":
    main()