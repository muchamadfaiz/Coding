# ABSTRACT BASE CLASS
# There is an issue with code before
# 1. we can create a stream object and call open method
#    -> why its an issue? because this class "Stream" is an abstract concept
#    in this example we want to open file from the file or network so we cant directly call from the base class
#    we always sub class it and then crate an instance from it
# 2. both subclass FileStream and NetworkStream have the same method that is read()
#    if next we want to create a different kind of stream
# To solve these issue we use "abstract base class"
from abc import ABC, abstractmethod #abstractmethod will be used as decorator


class InvalidOperationError(Exception):
    pass

#step 1 -> to make the class stream abstract we derive it to ABC Class
class Stream(ABC): # base class 
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError ("Stream is already open") 
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError ("Stream is already close") 
        self.opened = False

    @abstractmethod #step 2 -> to define the common interface for all stream, we want all stream have read method()
    def read(self):
        pass
    
    
class FileStream(Stream): # subclass 
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream): # subclass
    def read(self):
        print("Reading data from a network")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory")


# stream = Stream()
stream = MemoryStream()
stream.read()