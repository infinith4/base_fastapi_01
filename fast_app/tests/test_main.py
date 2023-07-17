# from fastapi import FastAPI
# from fastapi.testclient import TestClient

# app = FastAPI()

# #@pytest.fixture(name="root")
# @app.get("/")
# async def read_main():
#     return {"msg": "Hello World"}


# client = TestClient(app)

# #@pytest.fixture(name="main")
# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"msg": "Hello World"}

## https://fastapi.tiangolo.com/ja/tutorial/testing/
from fastapi.testclient import TestClient

from fast_app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_read_items():
    response = client.get("/items/1?q=test")
    assert response.status_code == 200
    assert response.json() == {
                    "item_id": 1,
                    "q": "test"
                }
