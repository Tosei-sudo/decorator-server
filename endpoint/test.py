import json
from decsvr import DecServerRouter

router = DecServerRouter.DecServerRouter()

@router.get('/data', content_type='application/json')
def data(request_info):
    return json.dumps({'data': 'Hello, World!'})

@router.get('/data2', content_type='application/json')
def data2(request_info):
    return json.dumps({'data': 'Hello!!, World!'})