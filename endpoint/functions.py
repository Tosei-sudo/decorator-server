try:
    from decsvr import DecServerRouter, ContentType
except ImportError:
    from ..decsvr import DecServerRouter, ContentType

router = DecServerRouter.DecServerRouter()

data = {
    "items": [
        {"item_id": "1", "item_name": "Item 1"},
        {"item_id": "2", "item_name": "Item 2"}
    ]
}

@router.get('/items', ContentType.APPLICATION_JSON)
def test(request_info):
    return data['items']