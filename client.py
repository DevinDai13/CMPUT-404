import socket

HOST = "www.google.com"
PORT = 80

BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\n\r\n"

def connect_socket(addr):
    (family, socketype, proto, cannoname, sockaddr) = addr
    try:
        s = socket.socket(family, socketype, proto) #get TCP connection
        s.connect(sockaddr)
        s.sendall(payload.encode()) #request the page
        full_data = b"" #(send using byte. cant use string)
        while True: # infincte loop for keeps receiving data, once all the data has been received, you get an empty string, loop breaks
            data = s.recv(BUFFER_SIZE)
            if not data:
               break
            full_data += data

        print(full_data)#print whatever we receive to terminal
        
    except:
        print("No connection was established")
        pass
    finally:
        s.close()

def main():
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
    addr = addr_info[0]
    connect_socket(addr)

if __name__ == "__main__":
    main()
