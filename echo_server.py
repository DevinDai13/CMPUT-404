import socket, time

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(2) #can only handle 2 clients

        while True:
            conn, addr = s.accept()
            print(addr)
            with conn:
                print(conn)#print out the connection 
                print(addr)#print the connected IP address
                full_data = b""
                while True:
                    data = conn.recv(BUFFER_SIZE)#what we receive from the client
                    if not data:
                        break
                    full_data += data
                    conn.close()

                conn.sendall(full_data)
                print(full_data) #print whatever we received from the client as the server

if __name__ == "__main__":
    main()