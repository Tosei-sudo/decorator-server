from handler import BasicHandler

class DecServerHandler(BasicHandler):
    def handle_get_request(self, request_info):
        endpoints = self.server.__get_endpoints__

        for path in endpoints.keys():
            if request_info.path == path:
                func, content_type = endpoints[path]
                
                self.send_http_response(200, content_type, func(request_info))
                return
        self.send_http_response(404, 'text/plain', 'Not Found')

    def handle_post_request(self, request_info):
        endpoints = self.server.__post_endpoints__

        for path in endpoints.keys():
            if request_info.path == path:
                func, content_type = endpoints[path]
                
                self.send_http_response(200, content_type, func(request_info))
                return
        self.send_http_response(404, 'text/plain', 'Not Found')
