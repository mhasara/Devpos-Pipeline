from app import     App
def test_home():
    client = App.test_client()
    response = App.test_client().get('/')
    assert response.status_code == 200
    assert b'Hello World' in response.data  