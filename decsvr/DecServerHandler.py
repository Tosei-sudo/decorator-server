import os

try:
    from decsvr.BasicHandler import BasicHandler

    import decsvr.HttpException as HttpException
    import decsvr.ContentType as ContentType
except ImportError:
    from BasicHandler import BasicHandler

    import HttpException
    import ContentType

class DecServerHandler(BasicHandler):
    def check_params(self, request_info, reqiure_params):
        for param in reqiure_params:
            if param not in request_info.query:
                raise HttpException.Http400MissingParameterException(param)
        return

    def handle_get_request(self, request_info):
        try:
            endpoints = self.server.__get_endpoints__

            for path in endpoints.keys():
                if request_info.path == path:
                    func, content_type, reqiure_params = endpoints[path]
                    
                    self.check_params(request_info, reqiure_params)
                    self.send_http_response(200, content_type, func(request_info))
                    
                    return
            
            if self.server.__resoleve_files__:
                self.send_file(request_info)
            else:
                raise HttpException.Http404Exception()
        except HttpException.HttpRedirectException as e:
            self.send_http_response(e.code, ContentType.PLANE_TEXT, e.location, {'Location': e.location})
        except HttpException.HttpException as e:
            self.send_http_response(e.code, ContentType.PLANE_TEXT, e.message)
        except Exception as e:
            self.send_http_response(500, ContentType.PLANE_TEXT, 'Internal Server Error')

    def handle_post_request(self, request_info):
        try:
            endpoints = self.server.__post_endpoints__

            for path in endpoints.keys():
                if request_info.path == path:
                    func, content_type, reqiure_params = endpoints[path]
                    
                    self.send_http_response(200, content_type, func(request_info))
                    return
            raise HttpException.Http404Exception()
        except HttpException.HttpException as e:
            self.send_http_response(e.code, ContentType.PLANE_TEXT, e.message)
        except Exception as e:
            self.send_http_response(500, ContentType.PLANE_TEXT, 'Internal Server Error')

    def send_file(self, request_info):
        try:
            file_path = request_info.path[1:]
            
            if not os.path.isfile(file_path):
                raise HttpException.Http404Exception()
            
            with open(file_path, 'rb') as file:
                content = file.read()

            self.send_http_response(200, ContentType.get_content_type_by_file(file_path), content)
        except IOError:
            raise HttpException.Http500Exception()