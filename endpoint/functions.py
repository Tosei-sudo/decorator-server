from decsvr import DecServerRouter

router = DecServerRouter.DecServerRouter()

@router.get('/test')
def test(request_info):
    return "<h1>Test</h1>"