from decsvr import DecServer

server = DecServer.DecServer(8000, True)

from endpoint import functions
from endpoint import test

if __name__ == '__main__':
    server.incude_router(functions.router)
    server.incude_router(test.router)
    
    server.start()