import socket
class LazyConnection(object):
    def __init__(self, address, family=socket.AF_INET,
                 socktype=socket.SOCK_STREAM):
        self.address = address
        self.family = family
        self.socktype = socktype
        self.sock  =  None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket.socket(self.family, self.socktype)
        self.sock.connect(self.address)
        
        return self.sock
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None    
        print("Connection closed")


from functools import partial

conn = LazyConnection(('www.python.org', 80))
# Connection closed
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.__exit__() executes: connection closed