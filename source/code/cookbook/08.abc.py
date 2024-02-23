from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass

class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass

def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    pass

import io

# Register the built-in I/O classes as supporting our interface
f = open(__file__, 'r')
print(isinstance(f, IStream))
IStream.register(io.IOBase)

# Open a normal file and type check

print(isinstance(f, IStream)) # Returns True