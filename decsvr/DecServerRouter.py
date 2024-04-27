class DecServerRouter():
    __get_endpoints__ = {}
    __post_endpoints__ = {}
    
    def get(self, path, content_type = 'text/html'):
        def wrapper(func):
            self.__get_endpoints__[path] = (func, content_type)
            return func
        return wrapper
    
    def post(self, path, content_type = 'text/html'):
        def wrapper(func):
            self.__post_endpoints__[path] = (func, content_type)
            return func
        return wrapper