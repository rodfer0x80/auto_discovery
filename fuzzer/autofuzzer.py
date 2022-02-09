import socket


class Autofuzzer:
    def __init__(self, server: str, port: int):
        self.server = server
        self.port = port
        self.conn = self.connect(self.server, self.port)


    def connect(self):
        try:
            self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            sys.stderr.write("[!] Error creating socket object\n")
        try:
            self.conn.connect((server, port))
        except:
            sys.stderr.write("[!] Error estabilishing socket conection\n")


    def refresh_connection(self):
        try:
            self.conn.close()
        except:
            sys.stderr.write("[!] Error closing socket connection\n")
        self.connect()


    def overflow_input(num_chars=128):
        for i in range(1, num_chars):
        try:
            self.read_until()
            data = 'A' * i + '\n'
            data = bytes(data, encoding='utf-8')
            self.conn.send(data)
        except:
            print(f"[*] Server crashed with input size {i}")
        finally:
            self.conn.refresh()


    def read_until(self, delim=b':'):    
        buf = b''
        while not buf.endswith(delim):
            buf += self.conn.recv(1)
        return buf


if __name__ == '__main__':
    try:
        server = sys.argv[1]
        port = int(sys.argv[2])
    except:
        sys.stderr.write("Usage: autofuzzer.py <server> <port>\n")
        exit(1)
    output = ""
    print(output)
    exit(0)
