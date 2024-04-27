from BaseHTTPServer import HTTPServer
from SocketServer import ThreadingMixIn

from DecServerHandler import DecServerHandler

class DecServer(ThreadingMixIn, HTTPServer):
    __get_endpoints__ = {}
    __post_endpoints__ = {}
    
    def __init__(self, port = 8000):
        HTTPServer.__init__(self, ('', port), DecServerHandler)

    def incude_router(self, router):
        self.__get_endpoints__.update(router.__get_endpoints__)
        self.__post_endpoints__.update(router.__post_endpoints__)
    
    def start(self):
        print('Starting WFS server on port %d...' % self.server_address[1])
        self.serve_forever()