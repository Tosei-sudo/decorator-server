try:
    import decsvr.ContentType as ContentType
except ImportError:
    import ContentType

class DecServerRouter():
    __get_endpoints__ = {}
    __post_endpoints__ = {}
    
    def get(self, path, content_type = ContentType.PLANE_TEXT, reqiure_params = []):
        def wrapper(func):
            self.__get_endpoints__[path] = (func, content_type, reqiure_params)
            return func
        return wrapper
    
    def post(self, path, content_type = ContentType.PLANE_TEXT, reqiure_params = []):
        def wrapper(func):
            self.__post_endpoints__[path] = (func, content_type, reqiure_params)
            return func
        return wrapper