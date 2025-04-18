
from .common.client import client, test_db

def test_integration_ton_api(client):
    response = client.post("http://testserver/v1/ton/", json={"trx": "TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g"})
    assert response.status_code == 200
    data = response.json()
    assert data["trx"] == "TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g"
    response = client.get("http://testserver/v1/ton/?limit=100")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["trx"] == "TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g"


