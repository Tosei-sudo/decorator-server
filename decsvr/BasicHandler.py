import json

try:
    # Python 3
    from urllib.parse import urlparse, parse_qs
    
    from http.server import BaseHTTPRequestHandler
    import decsvr.ContentType as ContentType
except ImportError:
    # Python 2
    from urlparse import urlparse, parse_qs

    from BaseHTTPServer import BaseHTTPRequestHandler
    import ContentType

class RequestInfo(object):
    def __init__(self, handler):
        self.headers = handler.headers
        
        url = urlparse(handler.path)
        
        self.path = url.path
        self.query = parse_qs(url.query)
        self.full_path = handler.path
        
        self.headers = handler.headers
        
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length == 0:
                content_length = int(self.headers.get('content-length', 0))
            self.body = handler.rfile.read(content_length)
        except:
            self.body = None

class BasicHandler(BaseHTTPRequestHandler):
    def send_http_response(self, status_code = 200, content_type = ContentType.PLANE_TEXT, content = None, extend = {}):
        
        if content_type == ContentType.APPLICATION_JSON:
            content = json.dumps(content)

        self.send_response(status_code)
        
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        
        if content:
            self.send_header('Content-Length', str(len(content)))        
        self.send_header('Connection', 'keep-alive')
        self.send_header('Last-Modified', self.date_time_string())
        
        self.send_header('Content-type', ContentType.get_mime_by_content_code(content_type))
        
        for key in extend.keys():
            self.send_header(key, extend[key])
        
        self.end_headers()
        
        try:
            content = bytes(content, 'UTF-8')
        except:
            pass
        
        self.wfile.write(content)

    def do_GET(self):
        self.handle_get_request(RequestInfo(self))
    
    def do_POST(self):
        self.handle_post_request(RequestInfo(self))

    def do_PUT(self):
        self.handle_put_request(RequestInfo(self))

    def do_DELETE(self):
        self.handle_delete_request(RequestInfo(self))
    
    def do_OPTIONS(self):
        self.send_http_response(200, ContentType.PLANE_TEXT, 'OK')