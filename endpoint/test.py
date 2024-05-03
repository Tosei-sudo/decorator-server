# coding: utf-8
try:
    from decsvr import DecServerRouter, ContentType, HttpException
except ImportError:
    from ..decsvr import DecServerRouter, ContentType, HttpException

router = DecServerRouter.DecServerRouter()

@router.get('/data', ContentType.APPLICATION_JSON)
def data(request_info):
    return {'data': u'Hello, Worldあ!'}

@router.get('/redirect')
def data(request_info):
    raise HttpException.HttpRedirectException('http://www.google.com')

@router.get('/data2/{id}', ContentType.APPLICATION_JSON)
def data2(request_info):
    return {'data': request_info.query}